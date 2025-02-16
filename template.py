import os 
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format="[%(asctime)s] : %(message)s")


project_name = "textSummarizer"

list_of_files = [
    ".github/workflows/.gitkeep",
    "template/index.html",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "dvc.yaml",
    "config/config.yaml",
    "params.yaml",
    "research/test.ipynb",
    "setup.py",
    "app.py",
    "main.py",
    "DockerFile",
    "requirements.txt"
]


for i in list_of_files:
    filepath = Path(i)

    # for separating file and folder 
    file_dir , file_name = os.path.split(filepath)

    if file_dir != "":
        os.makedirs(file_dir , exist_ok=True)
        logging.info(f"Created the directory: {file_dir} for the file : {file_name}")


    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath , "w") as f:
            pass
            logging.info(f"Created the empty file : {file_name}")

    else:
        logging.info(f"{file_name} :  already exists")
