from pathlib import Path
import os
import pickle
import argparse

from fastapi import FastAPI
import uvicorn

from .config import load_config, get_models_dir
from .logging import setup_logger

app = FastAPI()
logger = setup_logger("serve")

model = None


def load_model():
    global model

    models_dir = get_models_dir()

    if not models_dir.exists():
        raise RuntimeError(f"MODEL_DIR does not exist: {models_dir}")

    if not models_dir.is_dir():
        raise RuntimeError(f"MODEL_DIR is not a directory: {models_dir}")

    config = load_config()
    model_name = config["training"]["model_name"]

    model_path = models_dir / model_name

    if not model_path.exists():
        raise RuntimeError("Model file not found. Train first.")

    with open(model_path, "rb") as f:
        model = pickle.load(f)

    logger.info("Model loaded from %s", model_path.resolve())


@app.on_event("startup")
def startup_event():
    load_model()
    logger.info("Service started")


@app.get("/")
def health_check():
    return {"status": "ok", "message": "Model service is running"}


@app.post("/predict")
def predict(input_data: dict):
    return {
        "input": input_data,
        "prediction": "dummy_output",
        "model_version": model.get("version", "unknown"),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=None)
    args = parser.parse_args()

    # Priority order:
    # 1. CLI argument
    # 2. Environment variable
    # 3. Default 8000
    port = args.port or int(os.getenv("PORT", 8000))

    logger.info("Starting server on port %s", port)

    uvicorn.run(
        "src.model_service.serve:app",
        host="0.0.0.0",
        port=port,
        reload=False,
    )


if __name__ == "__main__":
    main()