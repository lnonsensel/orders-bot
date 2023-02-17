import logging
from datetime import datetime
from config import log_dir_path

curr = datetime.now().strftime('%H.%M.%S.%d.%m.%Y')
logging.basicConfig(level = logging.INFO, filename = f'{log_dir_path}/{curr}log.log', filemode = 'a', format = "%(asctime)s %(levelname)s %(message)s")
