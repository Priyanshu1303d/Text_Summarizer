import os 
import sys
import logging

log_string =  "[%(asctime)s : %(levelname)s : %(module)s  : %(message)s]"

logs_dir = "logs"
logs_filepath = os.path.join(logs_dir , "runnning_logs.log")
os.makedirs(logs_dir , exist_ok=True)

logging.basicConfig(
    level = logging.INFO,
    format = log_string,

    handlers =[
        logging.FileHandler(logs_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)


logger = logging.getLogger("textSummarizerLogger")