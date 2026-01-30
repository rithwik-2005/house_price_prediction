import sys
from src.house_price_prediction.logging.logger import logger
from src.house_price_prediction.exception.exception import CustomException
from src.house_price_prediction.config.configuration import ConfigurationManager
from src.house_price_prediction.components.data_validation import DataValidation


class DataValidationPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            logger.info("====== Data Validation Pipeline Started ======")

            # Load configuration
            config_manager = ConfigurationManager()
            data_validation_config = config_manager.get_data_validation_config()

            # Run validation
            data_validation = DataValidation(data_validation_config)
            validation_status = data_validation.initiate_data_validation()

            if not validation_status:
                raise Exception("Data validation failed. Check validation logs.")

            logger.info("====== Data Validation Pipeline Completed ======")

        except Exception as e:
            logger.error("Data Validation Pipeline failed")
            raise CustomException(e, sys)
