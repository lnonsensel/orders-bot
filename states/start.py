from cfg.bot_cfg import dp
from aiogram import types
from StatesClass import UserStates

@dp.message_handler(commands=['start', 'begin'])
async def start(message: types.Message):
    await message.answer('Добро пожаловать')
    await UserStates.reg.set()