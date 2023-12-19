import sys
from datetime import datetime
import os
import logging

format_str="[%(asctime)s : %(levelname)s : %(module)s : %(message)s]"

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%S')}"

log_path=os.path.join(os.getcwd(), "LOG", LOG_FILE)

os.makedirs(log_path, exist_ok=True)

LOG_FILE_PATH=os.path.join(log_path, LOG_FILE)

logging.basicConfig(level=logging.INFO, format=format_str,
                    handlers=[logging.FileHandler(LOG_FILE_PATH),
                              logging.StreamHandler(sys.stdout)
                              ])
logger=logging.getLogger("wafer_project")