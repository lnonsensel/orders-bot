from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from russian import *

menu_all = [menu_b1_text, menu_b2_text, menu_b3_text]
menu_b1 = KeyboardButton(menu_b1_text)
menu_b2 = KeyboardButton(menu_b2_text)
menu_b3 = KeyboardButton(menu_b3_text)
kb_menu = ReplyKeyboardMarkup(resize_keyboard=True)
kb_menu.add(menu_b1,menu_b2,menu_b3)