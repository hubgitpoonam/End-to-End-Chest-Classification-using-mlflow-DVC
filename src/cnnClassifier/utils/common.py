import os
import json
import base64
import joblib
import yaml

from typing import Any
from pathlib import Path
from box.exceptions import BoxValueError
from box import ConfigBox

from cnnClassifier import logger


def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns a ConfigBox object.

    Args:
        path_to_yaml (Path): Path to the YAML file.

    Raises:
        ValueError: If the YAML file is empty.

    Returns:
        ConfigBox: Parsed YAML content as a ConfigBox.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file loaded successfully from: {path_to_yaml}")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("YAML file is empty")
    except Exception as e:
        raise e


def create_directories(path_to_directories: list, verbose: bool = True):
    """
    Creates a list of directories.

    Args:
        path_to_directories (list): List of directory paths.
        verbose (bool): If True, logs directory creation info.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")


def save_json(path: Path, data: dict):
    """
    Saves a dictionary to a JSON file.

    Args:
        path (Path): Path to save JSON.
        data (dict): Dictionary data to save.
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"JSON file saved at: {path}")


def load_json(path: Path) -> ConfigBox:
    """
    Loads JSON data and returns it as a ConfigBox.

    Args:
        path (Path): Path to the JSON file.

    Returns:
        ConfigBox: Data loaded from JSON.
    """
    with open(path) as f:
        content = json.load(f)
    logger.info(f"JSON file loaded successfully from: {path}")
    return ConfigBox(content)


def save_bin(data: Any, path: Path):
    """
    Saves data as a binary file using joblib.

    Args:
        data (Any): Data to serialize.
        path (Path): Path to save the binary file.
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"Binary file saved at: {path}")

def get_size(path: Path) -> str:
    """Get the size of a file in KB."""
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"{size_in_kb} KB"

def decode_image(img_string: str, file_name: str) -> None:
    """Decode a base64 string and write it to an image file."""
    img_data = base64.b64decode(img_string)
    with open(file_name, "wb") as file:
        file.write(img_data)

def encode_image_to_base64(image_path: str) -> bytes:
    """Read an image file and encode it as base64."""
    with open(image_path, "rb") as file:
        return base64.b64encode(file.read())