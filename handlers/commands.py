from main import bot, dp  #, anti_flood
from aiogram.types import Message, CallbackQuery
from keyboards.inline_keyboard import kb1
# from asyncio import sleep
from tools.parser import pars_www
from datetime import *

@dp.message_handler(commands=['start'])
async def start_message(message: Message):
    text = "Это бот который дает полезную(нет) инфу о курсе валют."
    return await message.answer(text)

@dp.message_handler(commands=['menu'])
async def menu_command(m: Message):
    text = 'Это меню можно выбрать валютную пару'
    return await m.answer(text, reply_markup=kb1)

@dp.callback_query_handler(lambda x: x.data.split('-')[0] == 'para')
async def valuta_command(m: CallbackQuery):
    # print(m.data)
    # print(int(m.data.split('-')[1]))
    # print(await pars_www())
    res = int(m.data.split('-')[1])
    '''1. Узнавать появилось ли новое задание'''
    if res == 1:    
        list_v = await pars_www()
    # text_v = list_v[int(m.data.split('-')[1])]['symbol']
    # text_p = list_v[int(m.data.split('-')[1])]['price'][:-6]
    # print(list_v['data'])
        last_dz = list_v['data'][-1]
        print(last_dz)
        now = datetime.now()
        if last_dz['date'] == now.strftime("%d-%m-%Y"):
            await bot.delete_message(chat_id=m.from_user.id, message_id=m.message.message_id)
            await bot.send_message(chat_id=m.from_user.id, text = f"Есть новое задание от {str(last_dz['date'])}\n\n№{str(last_dz['id'])}:{str(last_dz['title'])}\n\nТекст задания: {str(last_dz['description'])}") 
        else:
            await bot.delete_message(chat_id=m.from_user.id, message_id=m.message.message_id)
            await bot.send_message(chat_id=m.from_user.id, text = f"Последнее задание от {str(last_dz['date'])}\n\n№{str(last_dz['id'])}:{str(last_dz['title'])}\n\nТекст задания: {str(last_dz['description'])}") 
    '''2. Получать текст задания (по id)'''
    if res == 2:
        await bot.delete_message(chat_id=m.from_user.id, message_id=m.message.message_id)
        await bot.send_message(chat_id=m.from_user.id, text = "Чтобы показать задание, введит 'id' и номер задания.\n Пример: 'id_25'")
    '''3. Отправлять ответ на задание'''
    if res == 3:
        await bot.delete_message(chat_id=m.from_user.id, message_id=m.message.message_id)
        await bot.send_message(chat_id=m.from_user.id, text = "Чтобы отправить ответ на задание, введитe 'id', номер задания, текст ответа.\n Пример: 'id_25_$$ текст ответа'")
    '''4. Отправлять задания в предложку'''
    if res == 4:
        await bot.delete_message(chat_id=m.from_user.id, message_id=m.message.message_id)
        await bot.send_message(chat_id=m.from_user.id, text = "Чтобы отправить задание в предложку, введитe 'new', заголовок задания, текст задания, начальный код, комментарий.\n Пример: 'new_$$ заголовок задания_$$ текст задания _$$ начальный код _$$ комментарий'")


    


