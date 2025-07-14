import os

from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format= '[%(asctime)s]: [%(message)s]')

project_name = "cnnClassifier"

list_of_files = [
    ".github/workflows/.gitkeep",

    # Source package structure
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/utils/__init__.py",

    # Configuration files
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",

    # Project root files
    "requirements.txt",
    "setup.py",

    # Notebooks and templates
    "research/trials.ipynb",
    "templates/index.html"
]

for filepath in list_of_files:
    path = Path(filepath)
    dir_path = path.parent

    # Create directory if it doesn't exist
    if dir_path != Path('.'):
        dir_path.mkdir(parents=True, exist_ok=True)
        logging.info(f"Creating directory: {dir_path} for the file: {path.name}")

    # Create empty file if it doesn't exist or is empty
    if not path.exists() or path.stat().st_size == 0:
        path.touch()
        logging.info(f"Creating empty file: {path}")
    else:
        logging.info(f"{path.name} already exists")