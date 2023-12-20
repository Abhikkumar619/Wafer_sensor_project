import yaml
import json
from ensure import ensure_annotations
from box import config_box
from pathlib import Path
from wafer_project import logger
import os
from box import ConfigBox
import dill

@ensure_annotations
def read_yaml(path_to_yaml: Path)-> ConfigBox: 
    try: 
        with open(path_to_yaml) as yaml_file: 
            content=yaml.safe_load(yaml_file)
            logger.info(f"Yaml file read sucessfully: {path_to_yaml}")
            
            return ConfigBox(content)
    except Exception as e: 
        raise e
        
@ensure_annotations
def create_directories(path_loc_list: list): 
    try: 
        for path in path_loc_list:
            os.makedirs(path, exist_ok=True)
            logger.info(f" Directories is created : {path}")
    except Exception as e: 
        raise e
    
@ensure_annotations
def save_json(path_loc: Path, Data: dict): 
    with open(path_loc) as f: 
        json.dump(Data, f)
    logger.info(f"Json file save sucessfully at: {path_loc}")


@ensure_annotations   
def load_json(path_loc: Path)-> config_box:
    try:  
        with open(path_loc) as f:
            content=json.load(f)
        logger.info(f"json file load sucessfully from path: {path_loc}")
        return ConfigBox(content)
    except Exception as e: 
        raise e
    

@ensure_annotations
def load_object(file_path: Path, obj):
    try:  
        with open(file_path, "wb") as file_obj: 
            dill.dump(obj, file_path)
            
    except Exception as e: 
        raise e
 
def load_object(file_path: Path): 
    try: 
        with open(file_path,'rb') as file_obj: 
            return dill.load(file_obj)
    except Exception as e: 
        raise e   
        
    