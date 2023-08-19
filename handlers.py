import asyncio
import logging
import sys
import os

from aiogram import Bot, Dispatcher, Router
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram import types

from bot_answers import *
from user_answers import *

token="6412831335:AAGBAvIVJKzY90o9-hdDbQoQR7elyJ1WQcs"
selfie_id='AgACAgIAAxkBAAPfZOEkW6-UBji0Aour7hqt26LfxY4AAjDLMRtWXglLEaOkTj1VPnkBAAMCAANzAAMwBA'
school_id='AgACAgIAAxkBAAPgZOEkcxEbNG1iHxlJlC5WyZ5Ht0oAArHLMRvRbAlLkreWOYy5eTcBAAMCAANzAAMwBA'

voice_gpt_id='AwACAgIAAxkBAAOEZODyIf6L9339drVxRYkuzPlNxnYAAsg0AALRbAFL-42ObnXdRIAwBA'
voice_sql_id='AwACAgIAAxkBAAOGZOENz0Wd8k7gRe09Bvk2Az3q7KQAArUyAAJWXglL5MYG0JKGbb4wBA'
voice_love_id='AwACAgIAAxkBAAOFZOEGGWOaq0hdqNIgJ6CjWGuigHcAAoYyAAJWXglLqBaSfI3X19YwBA'
# token = os.getenv("TOKEN")
# selfie_id = os.getenv("SELFIE_ID")
# school_id = os.getenv("SCHOOL_ID")
# voice_gpt_id = os.getenv("VOICE_GPT_ID")
# voice_sql_id = os.getenv("VOICE_SQL_ID")
# voice_love_id = os.getenv("VOICE_LOVE_ID")


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

# @router.message()
# async def scan_message(msg: types.Message):
#     document_id = msg.photo[0].file_id
#     file_info = await bot.get_file(document_id)
#     print(f'file_id: {file_info.file_id}')
#     print(f'file_path: {file_info.file_path}')
#     print(f'file_size: {file_info.file_size}')
#     print(f'file_unique_id: {file_info.file_unique_id}')


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
