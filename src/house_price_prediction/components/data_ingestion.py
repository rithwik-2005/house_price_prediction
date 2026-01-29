import sys
import pandas as pd
from pathlib import Path

from src.house_price_prediction.logging.logger import logger
from src.house_price_prediction.exception.exception import CustomException
from src.house_price_prediction.entity.config_entity import DataIngestionConfig
from src.house_price_prediction.utils.common import create_directories


class DataIngestion:
    """
    Handles data ingestion stage of the ML pipeline.
    Loads raw data and stores it in the artifacts directory.
    """

    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def initiate_data_ingestion(self) -> Path:
        try:
            logger.info("Starting data ingestion process")

            # Ensure ingestion directory exists
            create_directories([Path(self.config.root_dir)])

            # Load data
            source_file = Path(self.config.source_file)
            df = pd.read_csv(source_file)
            logger.info(f"Data successfully loaded from {source_file}")

            # Save to artifacts
            local_data_file = Path(self.config.local_data_file)
            df.to_csv(local_data_file, index=False)
            logger.info(f"Data saved to artifacts at {local_data_file}")

            return local_data_file

        except Exception as e:
            logger.error("Error occurred during data ingestion")
            raise CustomException(e, sys)
