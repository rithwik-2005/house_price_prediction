import sys
from src.house_price_prediction.logging.logger import logger
from src.house_price_prediction.exception.exception import CustomException
from src.house_price_prediction.config.configuration import ConfigurationManager
from src.house_price_prediction.components.model_trainer import ModelTrainer


class ModelTrainerPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            logger.info("==== Model Trainer Pipeline Started =====")

            # Load Configuration
            config_manager = ConfigurationManager()
            model_trainer_config = config_manager.get_model_trainer_config()

            # Run Training
            model_trainer = ModelTrainer(model_trainer_config)
            trainer_output = model_trainer.initiate_model_trainer()

            model_path = trainer_output["model_path"]
            metrics = trainer_output["metrics"]
            best_params = trainer_output["best_params"]

            logger.info(
                f"==== Model Trainer Pipeline Completed ======\n"
                f"Model Path: {model_path}\n"
                f"Metrics: {metrics}\n"
                f"Best Params: {best_params}"
            )

        except Exception as e:
            logger.error("Model Trainer Pipeline Failed")
            raise CustomException(e, sys)
