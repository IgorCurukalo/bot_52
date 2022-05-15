from main import bot, dp, anti_flood
from aiogram.types import Message
from validation.text import is_admin

@dp.message_handler(content_types=['text'])
async def default_text(message: Message):
    return await message.answer(text='Это стандартное сообщение')
