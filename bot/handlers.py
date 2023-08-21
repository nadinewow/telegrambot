from aiogram import Bot, Router
from aiogram.filters import CommandStart, Command
from aiogram import types

from answers import user_answers, bot_answers
from config import *

router = Router()


@router.message(CommandStart())
async def command_start_handler(message: types.Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    kb = [
        [types.KeyboardButton(text=user_answers.see_photos)],
        [types.KeyboardButton(text=user_answers.hobby_post)],
        [types.KeyboardButton(text=user_answers.send_voice)],

    ]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=kb)

    await message.answer(bot_answers.start_message, reply_markup=keyboard)


@router.message(lambda message: message.text == user_answers.see_photos)
async def send_photo(message: types.Message) -> None:
    await message.answer(bot_answers.see_photos)


@router.message(Command("selfie"))
async def send_selfie(message: types.Message, bot: Bot):
    await bot.send_photo(message.from_user.id, photo=selfie_id)


@router.message(Command("school_photo"))
async def send_school_photo(message: types.Message, bot: Bot):
    await bot.send_photo(message.from_user.id, photo=school_id)


@router.message(lambda message: message.text == user_answers.hobby_post)
async def send_hobby_post(message: types.Message):
    await message.answer(bot_answers.hobby_post)


@router.message(lambda message: message.text == user_answers.send_voice)
async def send_voice_message(message: types.Message):

    kb = [
        [types.InlineKeyboardButton(text=user_answers.gpt, callback_data="command_gpt")],
        [types.InlineKeyboardButton(text=user_answers.sql, callback_data='command_sql')],
        [types.InlineKeyboardButton(text=user_answers.love, callback_data='command_love')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)

    await message.answer(bot_answers.voice_message, reply_markup=keyboard)


@router.callback_query(lambda c: c.data == 'command_gpt')
async def process_callback_button1(callback_query: types.CallbackQuery, bot: Bot):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_voice(callback_query.from_user.id, voice=voice_gpt_id)


@router.callback_query(lambda c: c.data == 'command_sql')
async def process_callback_button1(callback_query: types.CallbackQuery, bot: Bot):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_voice(callback_query.from_user.id, voice=voice_sql_id)


@router.callback_query(lambda c: c.data == 'command_love')
async def process_callback_button1(callback_query: types.CallbackQuery, bot: Bot):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_voice(callback_query.from_user.id, voice=voice_love_id)


@router.message(Command("sourse_code"))
async def send_selfie(message: types.Message):
    await message.answer(bot_answers.sourse_link)
