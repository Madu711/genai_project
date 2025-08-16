from datetime import datetime
import logging
import os

Log_File = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

log_path = os.path.join(os.getcwd(), "logs")


os.makedirs(log_path, exist_ok=True)

Log_Filepath = os.path.join(log_path, Log_File)

logging.basicConfig(level=logging.INFO,
        filename=Log_Filepath, 
        format='[%(asctime)s] - %(levelname)s - %(message)s - %(lineno)d - %(name)s', 
        datefmt='%Y-%m-%d %H:%M:%S'
)