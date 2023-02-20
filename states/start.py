from cfg.bot_cfg import dp
from aiogram import types
from StatesClass import UserStates
from sql.sql_func import sql_get_all_users_ids
from reg import name
from keyboards.keyboards import kb_menu


@dp.message_handler(commands=['start', 'begin'])
async def start(message: types.Message):
    await message.answer('Добро пожаловать')

    if message.from_user.id in sql_get_all_users_ids():
        await message.answer('Меню', reply_markup=kb_menu)
        await UserStates.menu.set()
    else:
        await UserStates.reg.set()