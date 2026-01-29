import os
import yaml
from src.house_price_prediction.logging.logger import logger
import joblib
import json
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxError
import sys
from src.house_price_prediction.exception.exception import CustomException


'''ConfigBox is a small but very powerful utility that 
turns a YAML (or dict) configuration into an object with dot-notation access'''
#this function will read the yaml file and return the file in object format
#ensure annotations helps in maintain the datatype securely without mismatch

@ensure_annotations
def read_yaml(path_to_yaml: Path)->ConfigBox:
    try:
        with open(path_to_yaml) as file:
            content=yaml.safe_load(path_to_yaml)
            logger.info(f'yaml file:{path_to_yaml} loaded successfully')
            return ConfigBox(content)
    except Exception as e:
        raise CustomException(e,sys)
    
@ensure_annotations
def create_directory(path_to_dir:list,verbose=True):
    for path in path_to_dir:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f'created directory at :{path} successfully')


@ensure_annotations
def save_json(path: Path,data: dict):
    with open(path,'w') as file:
        json.dump(data,file,indent=2)
    logger.info(f'json file is saved successfully at :{path}')

@ensure_annotations
def load_json(path: Path):
    with open(path) as file:
        content=json.load(file)
    logger.info(f"json file loaded successfully from :{path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(path:Path,data:Any):
    joblib.dump(value=data,filename=path)
    logger.info(f'binary file saved at :{path}')

@ensure_annotations
def load_bin(path:Path):
    data=joblib.load(path)
    logger.info(f'binary file is loaded successfully')
    return data



    