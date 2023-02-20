from StatesClass import UserStates
from cfg.bot_cfg import dp 
from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from keyboards.keyboards import menu_b1_text,menu_b2_text,menu_b3_text


@dp.message_handler(lambda message: message.text == menu_b1_text, state = UserStates.menu)
async def menu(message: types.Message):
    UserStates.order.set()


@dp.message_handler(lambda message: message.text == menu_b2_text, state = UserStates.menu)
async def menu(message: types.Message):
    pass


@dp.message_handler(lambda message: message.text == menu_b3_text, state = UserStates.menu)
async def menu(message: types.Message):
    pass


@dp.message_handler(state = UserStates.menu)
async def menu(message: types.Message):
    pass

