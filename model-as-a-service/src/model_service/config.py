import os
from pathlib import Path
import yaml


# ---------- Environment variables (Docker-safe defaults) ----------

# Absolute paths inside the container (matches your volume mounts)
MODEL_DIR = os.getenv("MODEL_DIR", "/app/models/latest")
LOG_DIR   = os.getenv("LOG_DIR", "/app/logs")
APP_ENV   = os.getenv("APP_ENV", "dev")


# ---------- Optional: Fail fast only in production ----------

if APP_ENV == "prod":
    missing = [k for k, v in {
        "MODEL_DIR": MODEL_DIR,
        "LOG_DIR": LOG_DIR,
    }.items() if not v]

    if missing:
        raise RuntimeError(f"Missing required env vars in prod: {missing}")


# ---------- Project structure helpers ----------

def get_project_root() -> Path:
    """
    Returns project root.
    In Docker, this is always /app.
    Locally, this resolves relative to this file.
    """
    root = Path(__file__).resolve().parents[2]

    # If running inside Docker, prefer /app explicitly
    if Path("/app").exists():
        return Path("/app")

    return root


# ---------- Config loading ----------

def load_config() -> dict:
    """
    Loads YAML configuration file.
    """
    config_path = get_project_root() / "configs" / "config.yaml"

    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found at {config_path}")

    with open(config_path, "r") as file:
        return yaml.safe_load(file)


# ---------- Paths resolved using env vars ----------

def get_models_dir() -> Path:
    """
    Returns absolute models directory path.
    Creates it if it doesn't exist.
    """
    path = Path(MODEL_DIR)

    # If relative path was passed via env, anchor it to project root
    if not path.is_absolute():
        path = get_project_root() / path

    path.mkdir(parents=True, exist_ok=True)
    return path


def get_logs_dir() -> Path:
    """
    Returns absolute logs directory path.
    Creates it if it doesn't exist.
    """
    path = Path(LOG_DIR)

    # If relative path was passed via env, anchor it to project root
    if not path.is_absolute():
        path = get_project_root() / path

    path.mkdir(parents=True, exist_ok=True)
    return path