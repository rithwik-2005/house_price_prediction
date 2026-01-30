import sys
from src.house_price_prediction.logging.logger import logger
from src.house_price_prediction.exception.exception import CustomException
from src.house_price_prediction.config.configuration import ConfigurationManager
from src.house_price_prediction.components.data_ingestion import DataIngestion


class DataIngestionPipeline:
    """
    Orchestrates the data ingestion stage of the ML pipeline.
    """

    def __init__(self):
        pass

    def main(self):
        try:
            logger.info("===== Data Ingestion Pipeline Started =====")

            # Load configuration
            config_manager = ConfigurationManager()
            data_ingestion_config = config_manager.get_data_ingestion_config()

            # Run ingestion
            data_ingestion = DataIngestion(data_ingestion_config)
            data_path = data_ingestion.initiate_data_ingestion()

            logger.info(
                f"===== Data Ingestion Pipeline Completed =====\n"
                f"Ingested data path: {data_path}"
            )

        except Exception as e:
            logger.error("Data Ingestion Pipeline failed")
            raise CustomException(e, sys)
