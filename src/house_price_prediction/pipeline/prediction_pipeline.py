import sys
import pandas as pd
from pathlib import Path

from src.house_price_prediction.logging.logger import logger
from src.house_price_prediction.exception.exception import CustomException
from src.house_price_prediction.utils.common import load_bin


class PredictionPipeline:
    """
    Handles inference using the trained model.
    """

    def __init__(self, model_path: Path):
        self.model_path = model_path

    def predict(self, input_data: pd.DataFrame):
        try:
            logger.info("Starting prediction pipeline")

            # Load trained model
            model = load_bin(self.model_path)
            logger.info(f"Model loaded from {self.model_path}")

            # Generate predictions
            predictions = model.predict(input_data)

            logger.info("Prediction completed successfully")

            return predictions

        except Exception as e:
            logger.error("Error occurred during prediction")
            raise CustomException(e, sys)
