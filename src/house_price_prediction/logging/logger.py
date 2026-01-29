import os
import logging
from datetime import datetime

#custom file name to log file using time 
logs_filename=f"{datetime.now().strftime('%d-%m-%y_%S-%M-%H')}.log"
folder_name="logs"
root_dir=os.path.join(os.getcwd(),folder_name)
os.makedirs(root_dir,exist_ok=True)
logs_filepath=os.path.join(root_dir,logs_filename)
#set basicConfig for the logging class
logging.basicConfig(
    filename=logs_filename,
    format="[%(asctime)s] [%(name)s] [%(levelname)s]-[%(message)s]",
    level=logging.INFO
)

#create the object to the logging
logger=logging.getLogger("house_price_prediction")
