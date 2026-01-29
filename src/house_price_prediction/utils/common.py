import os
import yaml
from src.house_price_prediction.logging.logger import logger
import joblib
import json
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any,List
from box.exceptions import BoxError
import sys
from src.house_price_prediction.exception.exception import CustomException


'''ConfigBox is a small but very powerful utility that 
turns a YAML (or dict) configuration into an object with dot-notation access'''
#this function will read the yaml file and return the file in object format
#ensure annotations helps in maintain the datatype securely without mismatch

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        with open(path_to_yaml, "r", encoding="utf-8") as file:
            content = yaml.safe_load(file)
            logger.info(f"YAML file loaded successfully: {path_to_yaml}")
            return ConfigBox(content)
    except BoxError as e:
        logger.error("Error parsing YAML file")
        raise CustomException(e, sys)
    except Exception as e:
        logger.error("Unexpected error while reading YAML")
        raise CustomException(e, sys)

@ensure_annotations
def create_directories(paths: List[Path], verbose: bool = True) -> None:
    for path in paths:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created at: {path}")


@ensure_annotations
def save_json(path: Path, data: dict) -> None:
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)
    logger.info(f"JSON file saved at: {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    with open(path, "r", encoding="utf-8") as file:
        content = json.load(file)
    logger.info(f"JSON file loaded from: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(path: Path, data: Any) -> None:
    joblib.dump(data, path)
    logger.info(f"Binary file saved at: {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    data = joblib.load(path)
    logger.info(f"Binary file loaded from: {path}")
    return data


    