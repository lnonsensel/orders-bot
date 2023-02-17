from StatesClass import UserStates
from cfg.bot_cfg import dp 
from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from captchas.make_captcha import generate_captcha
from aiogram.types import inlin

@dp.message_handler(state = UserStates.reg)
async def reg(message: types.Message):
    await message.answer('Пройдите регистрацию')
    await message.answer('Введите ваше имя')
    await UserStates.name.set()


@dp.message_handler(regexp='\w+',state = UserStates.name)
async def name(message: types.Message, state: FSMContext):
    await message.answer('Введите номер телефона')
    await state.update_data(name = message.text)
    await UserStates.number.set()
@dp.message_handler(state = UserStates.name)
async def wrong_name(message:types.Message):
    await message.answer('Имя может состоять только из букв')


@dp.message_handler(regexp='^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$',state = UserStates.number)
async def number(message: types.Message, state: FSMContext):
    await message.answer('Регистрация закончена, введите номер с картинки')
    await state.update_data(number = message.text)
    captcha_image, key = generate_captcha()
    await message.answer_photo(captcha_image)
    await state.update_data(key = key)
    await UserStates.captcha.set()
@dp.message_handler(state = UserStates.number)
async def wrong_number(message: types.Message):
    await message.answer('Введите корректный номер телефона')


@dp.message_handler(state = UserStates.captcha)
async def captcha(message: types.Message, state: FSMContext):
    key = await state.get_data()
    key = key['key']
    if message.text == key:
        await message.answer('Пройдено. Вы в меню')
        await UserStates.menu.set()
    else:
        message.answer('Неверно. Попробуйте ещё раз' )
        captcha_image, key = generate_captcha()
        await message.answer_photo(captcha_image)
        await state.update_data(key = key)
