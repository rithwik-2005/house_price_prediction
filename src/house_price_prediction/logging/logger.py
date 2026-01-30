import os
import logging
from datetime import datetime

# Create logs filename with timestamp
logs_filename = f"{datetime.now().strftime('%d-%m-%y_%H-%M-%S')}.log"

# Logs directory
folder_name = "logs"
root_dir = os.path.join(os.getcwd(), folder_name)
os.makedirs(root_dir, exist_ok=True)

# Full log file path
logs_filepath = os.path.join(root_dir, logs_filename)

# Configure logging
logging.basicConfig(
    filename=logs_filepath,   
    format="[%(asctime)s] [%(name)s] [%(levelname)s] - %(message)s",
    level=logging.INFO
)

# Create logger object
logger = logging.getLogger("house_price_prediction")
