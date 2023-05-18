from aiogram import types

from keyboards import start_command_keyboard
from utils import BotResponsesConfig
from loader import dp, bot


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    # TODO add user register into DB
    await bot.send_message(message.from_user.id,
                           BotResponsesConfig.startResponse,
                           reply_markup=start_command_keyboard)


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_message(message.from_user.id,
                           BotResponsesConfig.helpResponse,
                           reply_markup=start_command_keyboard)
