import sys
import json
import pandas as pd
from pathlib import Path

from src.house_price_prediction.logging.logger import logger
from src.house_price_prediction.exception.exception import CustomException
from src.house_price_prediction.entity.config_entity import DataValidationConfig
from src.house_price_prediction.utils.common import create_directories


class DataValidation:
    """
    Performs schema-based validation on ingested data.
    """

    def __init__(self, config: DataValidationConfig):
        self.config = config

    def initiate_data_validation(self) -> bool:
        try:
            logger.info("Starting data validation process")

            # Ensure validation directory exists
            create_directories([Path(self.config.root_dir)])

            # Load data
            df = pd.read_csv(Path(self.config.local_data_file))
            all_columns = df.columns.tolist()

            validation_status = True
            missing_columns = []

            # Validate schema
            for col in self.config.all_schema:
                if col not in all_columns:
                    validation_status = False
                    missing_columns.append(col)

            if missing_columns:
                logger.error(f"Missing columns in dataset: {missing_columns}")
            else:
                logger.info("All required columns are present")

            # Write validation status
            status_file = Path(self.config.STATUS_FILE)
            with open(status_file, "w", encoding="utf-8") as file:
                json.dump(
                    {
                        "validation_status": validation_status,
                        "missing_columns": missing_columns,
                    },
                    file,
                    indent=2,
                )

            logger.info(f"Validation status saved at: {status_file}")

            return validation_status

        except Exception as e:
            logger.error("Error occurred during data validation")
            raise CustomException(e, sys)
