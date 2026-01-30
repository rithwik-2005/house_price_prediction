import sys
from src.house_price_prediction.logging.logger import logger
from src.house_price_prediction.exception.exception import CustomException
from src.house_price_prediction.config.configuration import ConfigurationManager
from src.house_price_prediction.components.data_transformation import DataTransformation


class DataTransformationPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            logger.info("===== Data Transformation Pipeline Started =====")

            # Load configuration
            config_manager = ConfigurationManager()
            data_transformation_config = config_manager.get_data_transformation_config()

            # Run transformation
            data_transformation = DataTransformation(data_transformation_config)
            train_data_path, test_data_path = data_transformation.initiate_data_transformation()

            logger.info(
                f"===== Data Transformation Pipeline Completed =====\n"
                f"Train data: {train_data_path}\n"
                f"Test data: {test_data_path}"
            )

        except Exception as e:
            logger.error("Data Transformation Pipeline failed")
            raise CustomException(e, sys)
