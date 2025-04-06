import logging
import os
from datetime import datetime

# Create logs directory
LOGS_DIR = os.path.join(os.getcwd(), "logs")
os.makedirs(LOGS_DIR, exist_ok=True)

# Create full log file path
LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
LOG_FILE_PATH = os.path.join(LOGS_DIR, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[%(asctime)s] [Line: %(lineno)d] [%(name)s] - [%(levelname)s] - %(message)s',
    level=logging.INFO
)

if __name__ == "__main__":
    logging.info("Logging has started.")
