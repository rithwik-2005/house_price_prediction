from pathlib import Path
import os
from dotenv import load_dotenv

from src.house_price_prediction.constant.constant import (
    CONFIG_FILE_PATH,
    SCHEMA_FILE_PATH,
    PARAMS_FILE_PATH,
)
from src.house_price_prediction.utils.common import read_yaml, create_directories
from src.house_price_prediction.entity.config_entity import (
    DataIngestionConfig,
    DataValidationConfig,
    DataTransformationConfig,
    ModelTrainerConfig,
    ModelEvaluationConfig,
)

load_dotenv()


class ConfigurationManager:
    def __init__(
        self,
        config_file: Path = CONFIG_FILE_PATH,
        schema_file: Path = SCHEMA_FILE_PATH,
        params_file: Path = PARAMS_FILE_PATH,
    ):
        self.config = read_yaml(config_file)
        self.schema = read_yaml(schema_file)
        self.params = read_yaml(params_file)

        create_directories([Path(self.config.artifacts_root)])

   
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([Path(config.root_dir)])

        return DataIngestionConfig(
            root_dir=Path(config.root_dir),
            source_file=Path(config.source_file),
            local_data_file=Path(config.local_data_file),
        )

   
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        create_directories([Path(config.root_dir)])

        return DataValidationConfig(
            root_dir=Path(config.root_dir),
            local_data_file=Path(config.local_data_file),
            STATUS_FILE=Path(config.STATUS_FILE),
            all_schema=self.schema.COLUMNS,
        )

  
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation
        create_directories([Path(config.root_dir)])

        return DataTransformationConfig(
            root_dir=Path(config.root_dir),
            load_data_file=Path(config.load_data_file),
            train_data_path=Path(config.train_data_path),
            test_data_path=Path(config.test_data_path),
            target_column=self.schema.TARGET_COLUMN,
            test_size=self.params.split.test_size,
            random_state=self.params.seed.random_state,
        )


    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        create_directories([Path(config.root_dir)])

        return ModelTrainerConfig(
            root_dir=Path(config.root_dir),
            train_data_path=Path(config.train_data_path),
            test_data_path=Path(config.test_data_path),
            model_file=Path(config.model_file),
            best_params_file=Path(config.best_params_file),
            metrics_file_name=Path(config.metrics_file_name
                                   ),
            target_column=self.schema.TARGET_COLUMN,
            alpha=self.params.models.ElasticNet.alpha,
            l1_ratio=self.params.models.ElasticNet.l1_ratio,
            random_state=self.params.seed.random_state,
        )


    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation
        create_directories([Path(config.root_dir)])

        return ModelEvaluationConfig(
            root_dir=Path(config.root_dir),
            test_data_path=Path(config.test_data_path),
            model_path=Path(config.model_path),
            metrics_file_name=Path(config.metrics_file_name),
            mlflow_uri=os.getenv("MLFLOW_TRACKING_URI"),
            all_params=self.params.models.ElasticNet,
        )
