import sys
import json
import pandas as pd
from pathlib import Path
from sklearn.linear_model import ElasticNet
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from src.house_price_prediction.logging.logger import logger
from src.house_price_prediction.exception.exception import CustomException
from src.house_price_prediction.utils.common import create_directories, save_bin
from src.house_price_prediction.entity.config_entity import ModelTrainerConfig


class ModelTrainer:
    """
    Trains ElasticNet model using GridSearchCV and saves:
    - trained model
    - best hyperparameters
    - training & test metrics
    """

    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def initiate_model_trainer(self):
        try:
            logger.info("Starting model training process")

            # Create model trainer directory
            create_directories([Path(self.config.root_dir)])

            # Load train & test data
            train_df = pd.read_csv(Path(self.config.train_data_path))
            test_df = pd.read_csv(Path(self.config.test_data_path))

            logger.info("Train and test data loaded successfully")

            # Split features and target
            X_train = train_df.drop(columns=[self.config.target_column])
            y_train = train_df[self.config.target_column]

            X_test = test_df.drop(columns=[self.config.target_column])
            y_test = test_df[self.config.target_column]

            # Define model
            model = ElasticNet(random_state=self.config.random_state)

            # Hyperparameter grid
            param_grid = {
                "alpha": self.config.alpha,
                "l1_ratio": self.config.l1_ratio
            }

            # GridSearch
            grid_search = GridSearchCV(
                estimator=model,
                param_grid=param_grid,
                scoring="r2",
                cv=5,
                n_jobs=-1
            )

            grid_search.fit(X_train, y_train)

            best_model = grid_search.best_estimator_
            best_params = grid_search.best_params_

            logger.info(f"Best parameters found: {best_params}")

            # Predictions
            y_train_pred = best_model.predict(X_train)
            y_test_pred = best_model.predict(X_test)

            # Metrics
            train_r2 = r2_score(y_train, y_train_pred)
            test_r2 = r2_score(y_test, y_test_pred)

            metrics = {
                "train_r2_score": train_r2,
                "test_r2_score": test_r2
            }

            logger.info(f"Training R2 Score: {train_r2}")
            logger.info(f"Test R2 Score: {test_r2}")

            # Save model
            save_bin(Path(self.config.model_file), best_model)

            # Save metrics
            with open(Path(self.config.metric_file_name), "w") as f:
                json.dump(metrics, f, indent=2)

            # Save best parameters
            with open(Path(self.config.best_params_file), "w") as f:
                json.dump(best_params, f, indent=2)

            logger.info("Model training completed successfully")

            return {
                "model_path": self.config.model_file,
                "metrics": metrics,
                "best_params": best_params
            }

        except Exception as e:
            logger.error("Error occurred during model training")
            raise CustomException(e, sys)
