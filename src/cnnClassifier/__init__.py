import os
import sys
import logging

# Define logging format
LOG_FORMAT = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"

# Define log directory and file path
LOG_DIR = "logs"
LOG_FILE_PATH = os.path.join(LOG_DIR, "running_logs.log")

# Create log directory if it doesn't exist
os.makedirs(LOG_DIR, exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format=LOG_FORMAT,
    handlers=[
        logging.FileHandler(LOG_FILE_PATH),
        logging.StreamHandler(sys.stdout)
    ]
)

# Get logger instance
logger = logging.getLogger("cnnClassifierLogger")
