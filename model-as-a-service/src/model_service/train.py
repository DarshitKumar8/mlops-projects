from pathlib import Path
import pickle
import os
import random
import numpy as np

from .config import get_models_dir, load_config
from .logging import setup_logger


def set_seed(seed: int) -> None:
    os.environ["PYTHONHASHSEED"] = str(seed)
    random.seed(seed)
    np.random.seed(seed)

    try:
        import torch
        torch.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False
    except ImportError:
        pass

    try:
        import tensorflow as tf
        tf.random.set_seed(seed)
    except ImportError:
        pass


def train_model() -> Path:
    config = load_config()
    logger = setup_logger("train")

    training_cfg = config["training"]

    model_name = training_cfg["model_name"]
    seed = training_cfg["seed"]

    set_seed(seed)

    logger.info("Starting training")
    logger.info("Seed: %s", seed)

    models_dir: Path = get_models_dir()
    model_path = models_dir / model_name

    logger.info("Output version directory: %s", models_dir.name)
    logger.info("Models directory: %s", models_dir.resolve())
    logger.info("Model path: %s", model_path.resolve())

    # ---- Dummy model (replace with real training logic) ----
    model = {
        "type": "dummy",
        "version_folder": models_dir.name,
        "seed_used": seed
    }

    with open(model_path, "wb") as f:
        pickle.dump(model, f)

    logger.info("Model saved at %s", model_path.resolve())

    return model_path


if __name__ == "__main__":
    train_model()