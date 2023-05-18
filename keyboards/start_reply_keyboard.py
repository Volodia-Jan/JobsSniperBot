from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_command_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
start_command_keyboard.row(KeyboardButton("Вакансії 👨‍💻"), KeyboardButton("Фільтри 🔎"))