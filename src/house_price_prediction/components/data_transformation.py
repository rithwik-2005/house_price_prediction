import sys
import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split

from src.house_price_prediction.logging.logger import logger
from src.house_price_prediction.exception.exception import CustomException
from src.house_price_prediction.utils.common import create_directories
from src.house_price_prediction.entity.config_entity import DataTransformationConfig


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def initiate_data_transformation(self):
        try:
            logger.info("Starting data transformation process")

            create_directories([Path(self.config.root_dir)])

            df = pd.read_csv(Path(self.config.load_data_file))
            logger.info(f"Data loaded from {self.config.load_data_file}")

            if self.config.target_column not in df.columns:
                raise ValueError(
                    f"Target column '{self.config.target_column}' not found in dataset"
                )

            train_df, test_df = train_test_split(
                df,
                test_size=self.config.test_size,
                random_state=self.config.random_state
            )

            train_df.to_csv(Path(self.config.train_data_path), index=False)
            test_df.to_csv(Path(self.config.test_data_path), index=False)

            logger.info(
                f"Data transformation completed. "
                f"Train data: {self.config.train_data_path}, "
                f"Test data: {self.config.test_data_path}"
            )

            return self.config.train_data_path, self.config.test_data_path

        except Exception as e:
            logger.error("Error occurred during data transformation")
            raise CustomException(e, sys)
