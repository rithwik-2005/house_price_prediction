import sys
from src.house_price_prediction.logging.logger import logger
from src.house_price_prediction.exception.exception import CustomException

from src.house_price_prediction.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.house_price_prediction.pipeline.data_validation_pipeline import DataValidationPipeline
from src.house_price_prediction.pipeline.data_transformation_pipeline import DataTransformationPipeline
from src.house_price_prediction.pipeline.model_trainer_pipeline import ModelTrainerPipeline
from src.house_price_prediction.pipeline.model_evaluation_pipeline import ModelEvaluationPipeline


def main():
    try:
        logger.info("========== ML PIPELINE STARTED ==========")

        DataIngestionPipeline().main()
        DataValidationPipeline().main()
        DataTransformationPipeline().main()
        ModelTrainerPipeline().main()
        ModelEvaluationPipeline().main()

        logger.info("========== ML PIPELINE COMPLETED SUCCESSFULLY ==========")

    except Exception as e:
        logger.error("========== ML PIPELINE FAILED ==========")
        raise CustomException(e, sys)


if __name__ == "__main__":
    main()
