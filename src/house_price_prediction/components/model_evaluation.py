import sys
import json
import pandas as pd
from pathlib import Path
from sklearn.metrics import r2_score
import mlflow
import mlflow.sklearn

from src.house_price_prediction.logging.logger import logger
from src.house_price_prediction.exception.exception import CustomException
from src.house_price_prediction.utils.common import create_directories, load_bin
from src.house_price_prediction.entity.config_entity import ModelEvaluationConfig


class ModelEvaluation:
    """
    Evaluates trained model on test data,
    logs metrics and parameters to MLflow,
    and saves evaluation metrics locally.
    """

    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def initiate_model_evaluation(self):
        try:
            logger.info("Starting model evaluation process")

            # Create evaluation directory
            create_directories([Path(self.config.root_dir)])

            # Set MLflow tracking URI
            mlflow.set_tracking_uri(self.config.mlflow_uri)

            # Load test data
            test_df = pd.read_csv(Path(self.config.test_data_path))
            logger.info(f"Test data loaded from {self.config.test_data_path}")

            # Load trained model
            model = load_bin(Path(self.config.model_path))
            logger.info(f"Model loaded from {self.config.model_path}")

            # Split features and target
            target_column = self.config.all_params.get("target_column")

            if target_column is None:
                raise ValueError("Target column not found in evaluation parameters")

            X_test = test_df.drop(columns=[target_column])
            y_test = test_df[target_column]

            # Predictions
            y_pred = model.predict(X_test)

            # Metric calculation
            test_r2 = r2_score(y_test, y_pred)
            metrics = {
                "test_r2_score": test_r2
            }

            logger.info(f"Test R2 Score: {test_r2}")

            # Save metrics locally
            with open(Path(self.config.metric_file_name), "w") as f:
                json.dump(metrics, f, indent=2)

            # Log to MLflow
            with mlflow.start_run():
                mlflow.log_params(self.config.all_params)
                mlflow.log_metric("test_r2_score", test_r2)
                mlflow.sklearn.log_model(model, "model")

            logger.info("Model evaluation completed successfully")

            return metrics

        except Exception as e:
            logger.error("Error occurred during model evaluation")
            raise CustomException(e, sys)
