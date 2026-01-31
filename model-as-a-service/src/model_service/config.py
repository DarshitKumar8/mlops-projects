import os
from pathlib import Path
import yaml


# ---------- Project structure helpers ----------

def get_project_root() -> Path:
    """
    Returns project root.
    In Docker, this is always /app.
    Locally, this resolves relative to this file.
    """
    root = Path(__file__).resolve().parents[2]

    if Path("/app").exists():
        return Path("/app")

    return root


# ---------- Config loading ----------

def load_config() -> dict:
    """
    Loads YAML configuration file.
    """
    config_path = get_project_root() / "configs" / "train_config.yaml"

    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found at {config_path}")

    with open(config_path, "r") as file:
        return yaml.safe_load(file)


# ---------- Auto Versioned Models Directory ----------

def get_models_dir() -> Path:
    """
    Automatically creates next versioned directory:

        models/v1
        models/v2
        models/v3
        ...

    Never overwrites previous versions.
    """
    config = load_config()

    base_dir = config["paths"]["models_dir"]
    base_path = Path(base_dir)

    if not base_path.is_absolute():
        base_path = get_project_root() / base_path

    base_path.mkdir(parents=True, exist_ok=True)

    # Detect existing version folders
    existing_versions = [
        int(p.name.replace("v", ""))
        for p in base_path.glob("v*")
        if p.is_dir() and p.name.replace("v", "").isdigit()
    ]

    next_version = max(existing_versions, default=0) + 1
    version_dir = base_path / f"v{next_version}"
    version_dir.mkdir(parents=True, exist_ok=True)

    return version_dir


def get_logs_dir() -> Path:
    """
    Returns logs directory path.
    """
    config = load_config()

    base_dir = config["paths"]["logs_dir"]
    base_path = Path(base_dir)

    if not base_path.is_absolute():
        base_path = get_project_root() / base_path

    base_path.mkdir(parents=True, exist_ok=True)

    return base_path