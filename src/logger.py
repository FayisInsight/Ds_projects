import logging
import os
from datetime import datetime

log_file = os.path.join(os.path.dirname(__file__), f"log_{datetime.now().strftime('%Y%m%d')}.log")
logging.basicConfig(filename=log_file, level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')
 

# Configure the logging settings
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

if __name__ == "__main__":
    logging.info("Logger is configured and the script is running.")
    