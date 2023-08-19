import asyncio
import logging
import sys
import os

from aiogram import Bot, Dispatcher, Router
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram import types

from bot.bot_answers import *
from user_answers import *

token = os.getenv("TOKEN")
selfie_id = os.getenv("SELFIE_ID")
school_id = os.getenv("SCHOOL_ID")
voice_gpt_id = os.getenv("VOICE_GPT_ID")
voice_sql_id = os.getenv("VOICE_SQL_ID")
voice_love_id = os.getenv("VOICE_LOVE_ID")


router = Router()
bot = Bot(token=token)


@router.message(CommandStart())
async def command_start_handler(message: types.Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    kb = [
        [types.KeyboardButton(text=see_photos_ans)],
        [types.KeyboardButton(text=hobby_post_ans)],
        [types.KeyboardButton(text=send_voice_ans)],

    ]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=kb)

    await message.answer(start_message, reply_markup=keyboard)


@router.message(lambda message: message.text == see_photos_ans)
async def send_photo(message: types.Message) -> None:
    await message.answer(see_photos)


@router.message(Command("selfie"))
async def send_selfie(message: types.Message):
    await bot.send_photo(message.from_user.id, photo=selfie_id)


@router.message(Command("school_photo"))
async def send_school_photo(message: types.Message):
    await bot.send_photo(message.from_user.id, photo=school_id)


@router.message(lambda message: message.text == hobby_post_ans)
async def send_hobby_post(message: types.Message):
    await message.answer(hobby_post)


@router.message(lambda message: message.text == send_voice_ans)
async def send_voice_message(message: types.Message):

    kb = [
        [types.InlineKeyboardButton(text=gpt_ans, callback_data="command_gpt")],
        [types.InlineKeyboardButton(text=sql_ans, callback_data='command_sql')],
        [types.InlineKeyboardButton(text=love_ans, callback_data='command_love')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)

    await message.answer(voice_message, reply_markup=keyboard)


@router.callback_query(lambda c: c.data == 'command_gpt')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_voice(callback_query.from_user.id, voice=voice_gpt_id)


@router.callback_query(lambda c: c.data == 'command_sql')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_voice(callback_query.from_user.id, voice=voice_sql_id)


@router.callback_query(lambda c: c.data == 'command_love')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_voice(callback_query.from_user.id, voice=voice_love_id)


@router.message(Command("sourse_code"))
async def send_selfie(message: types.Message):
    await message.answer(sourse_link)


async def main() -> None:
    dp = Dispatcher()
    dp.include_router(router)

    bot = Bot(token, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Bot stopped!")
