from src.model_service.logging import setup_logger

# Create logger once (not per function call)
logger = setup_logger("inference")


def predict(model: dict, data: str) -> str:
    """
    Run prediction using an already-loaded model.

    Args:
        model: Loaded model object (from serve.py)
        data: Input data for prediction

    Returns:
        Prediction result
    """
    logger.info("Running prediction")

    # Dummy prediction logic
    return f"prediction({data}) using [{model}]"