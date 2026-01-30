import sys
from src.house_price_prediction.logging.logger import logger
from src.house_price_prediction.exception.exception import CustomException
from src.house_price_prediction.components.model_evaluation import ModelEvaluation
from src.house_price_prediction.config.configuration import ConfigurationManager


class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            logger.info("==== Model Evaluation Pipeline Started ======")

            # Load configuration
            config_manager = ConfigurationManager()
            model_evaluation_config = config_manager.get_model_evaluation_config()

            # Run evaluation
            model_evaluation = ModelEvaluation(model_evaluation_config)
            evaluation_output = model_evaluation.initiate_model_evaluation()

            logger.info(
                f"==== Model Evaluation Pipeline Completed ======\n"
                f"Metrics: {evaluation_output}"
            )

        except Exception as e:
            logger.error("Model Evaluation Pipeline Failed")
            raise CustomException(e, sys)
