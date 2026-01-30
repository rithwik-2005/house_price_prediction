from dataclasses import dataclass
from pathlib import Path
from typing import Dict,Any,List

"""@dataclass is a Python decorator that automatically generates 
boilerplate code for classes whose main purpose is to store data."""

@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_file: Path
    local_data_file: Path

@dataclass
class DataValidationConfig:
    root_dir: Path
    local_data_file: Path
    STATUS_FILE: Path
    all_schema: Dict[str,Any]

@dataclass
class DataTransformationConfig:
    root_dir: Path
    load_data_file: Path
    test_data_path: Path
    train_data_path: Path
    target_column: str
    test_size: float
    random_state: int

@dataclass
class ModelTrainerConfig:
    root_dir: Path
    test_data_path: Path
    train_data_path: Path
    model_file: Path
    best_params_file: Path
    metrics_file_name: Path
    target_column: str
    alpha: List[float]
    l1_ratio: List[float]
    random_state: int


@dataclass
class ModelEvaluationConfig:
    root_dir: Path
    test_data_path: Path
    model_path: Path
    metrics_file_name: Path
    mlflow_uri: str
    all_params: Dict[str,Any]
    target_column: str



