'''Написать бота с помощью которого можно взаимодействовать с этим сайтом.
Что должен уметь бот:

1. Узнавать появилось ли новое задание
2. Получать текст задания (по id)
3. Отправлять ответ на задание
4. Отправлять задания в предложку
5. Выложить бота на GitHub'''

import asyncio
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher, executor
from config import BOT_TOKEN, admin_id

loop = asyncio.get_event_loop
bot = Bot(BOT_TOKEN, parse_mode="HTML")
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage, loop=loop)

async def anti_flood(*args, **kwargs):
    m = args[0]
    await m.answer("Не флуди...")

async def send_to_admin(dp):
    await bot.send_message(chat_id=admin_id, text=f"start")

if __name__ == "__main__":
    from handlers.commands import dp
    executor.start_polling(dp, on_startup=send_to_admin)
    import handlers