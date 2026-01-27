from pathlib import Path
import pickle

from .config import get_models_dir, load_config
from .logging import setup_logger


def train_model() -> Path:
    logger = setup_logger("train")

    # -------- Use config helper (single source of truth) --------
    models_dir: Path = get_models_dir()
    models_dir.mkdir(parents=True, exist_ok=True)

    if not models_dir.is_dir():
        raise RuntimeError(f"Models dir is not a directory: {models_dir}")
    # -----------------------------------------------------------

    config = load_config()
    model_name = config["training"]["model_name"]

    model_path = models_dir / model_name

    logger.info("Starting training")
    logger.info("Models directory: %s", models_dir.resolve())
    logger.info("Model path: %s", model_path.resolve())

    # ---- Dummy model (your real training logic goes here) ----
    model = {
        "type": "dummy",
        "version": 1
    }

    with open(model_path, "wb") as f:
        pickle.dump(model, f)

    logger.info("Model saved at %s", model_path.resolve())

    return model_path


if __name__ == "__main__":
    train_model()