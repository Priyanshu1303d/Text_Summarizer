import os 
from pathlib import Path 
import yaml 
from textSummarizer.logging import logger
from box import ConfigBox
from typing import Any
from ensure import ensure_annotations
from box.exceptions import BoxValueError




@ensure_annotations
def read_yaml(path_to_yaml : Path) -> ConfigBox :
    '''
        reads the yaml file and Returns

        Args:
            path_to_yaml : path like input
        Raises: 
            ValueError : if yaml file is empty
            e: empty file 
        Returns: 
            ConfigBox : ConfigBox Type 
    '''

    try:
        with open(path_to_yaml) as f:
            content = yaml.safe_load(f)
            logger.info(f"yaml file {path_to_yaml} was read succesfully")
            return ConfigBox(content)
        
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e: 
        raise e
    

@ensure_annotations
def create_directories(path_of_directories: Path , verbose = True):
    '''
        Creates list of the Directories 

        Args: 
            path_of_directories: list of the path of the directories
            ignore_log(bool , optional) : ignore if multiple directories is to be created. Defaults to False
    '''

    for i in path_of_directories:
        os.makedirs(i , exist_ok=True)
        if verbose :
            logger.info(f"Created directory at : {i}")


@ensure_annotations
def get_size(path : Path) -> str:
    '''
        get size in KB


        Args:
            path : Path of the file
        Returns: 
            str : Size in KB
    ''' 
    size_in_KB = round(os.path.getsize(path)/1024)
    return f"~{size_in_KB} in KB"