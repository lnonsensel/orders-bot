from aiogram.dispatcher.filters.state import State, StatesGroup


class UserStates(StatesGroup):
    reg = State()
    name = State()
    number = State()
    captcha = State()
    menu = State()
    order = State()