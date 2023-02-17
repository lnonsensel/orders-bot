from aiogram.dispatcher import Dispatcher
from aiogram import Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import bot_api_main

storage = MemoryStorage()
bot = Bot(bot_api_main)
dp = Dispatcher(bot, storage=storage)
