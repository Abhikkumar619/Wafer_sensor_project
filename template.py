from pathlib import Path
import os
import sys
import logging

logging.basicConfig(level=logging.INFO, format="[%(asctime)s : %(message)s:]")


project_name= "wafer_project"

list_of_file=[
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/constant/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "application.py",
    "main.py",
    "requirement.txt",
    "setup.py",
    "research/Experiment.ipynb",
    "templates/index.html"
]

for path in list_of_file:
    file_dir, file_name=os.path.split(path)
    # logging.info(f"File dir: {file_dir}, file_name {file_name}")
    
    if file_dir !="": 
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"file_direcories is created: {file_dir} for file : {file_name}")
        
    if (not os.path.exists(path) or os.path.getsize(path)):
        with open(path, 'w') as f:
            pass
        logging.info(f"File is created: {path}")
        
    else: 
        logging.info(f"File is already exists: {path}")
        