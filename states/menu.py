from StatesClass import UserStates
from cfg.bot_cfg import dp 
from aiogram import types
from aiogram.dispatcher.storage import FSMContext


@dp.message_handler(state = UserStates.menu)
async def menu(message: types.Message):
    print('menu active')

