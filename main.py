import sys 
import pathlib

current_path = pathlib.Path(__file__).parent.resolve()
sys.path.append(f'{current_path}')
sys.path.append(f'{current_path}/cfg')
sys.path.append(f'{current_path}/logs')
sys.path.append(f'{current_path}/states')
sys.path.append(f'{current_path}/sql')

from aiogram import executor
from states import *
from cfg.bot_cfg import dp
from sql.sql_setup import sql_setup
from cfg import logs_config
from art import tprint


def on_startup():
    sql_setup()
    tprint('bot online', font = 'bell')
    pass

executor.start_polling(dp, skip_updates=True, on_startup=on_startup())