from email import message
from main import bot, dp, anti_flood
from aiogram.types import Message
from validation.text import return_homework_id, homework_answer, new_homework
from tools.parser import pars_www
import requests
from config import User_Agent, Url_api

'''Узнать задание по id'''
@dp.message_handler(lambda x: return_homework_id(x))
async def first_custom_handler(m:Message):
    msg = m.text
    list_m = msg.split('_')
    # print(msg)
    list_v = await pars_www()
    list_v = list_v['data']
    for n,i in  enumerate(list_v):
        # print(i['id'], list_m[1])
        if int(i['id']) == int(list_m[1]):
            await bot.send_message(chat_id=m.from_user.id, text = f"Задание от {str(list_v[n]['date'])}\n\n№{str(list_v[n]['id'])}:{str(list_v[n]['title'])}\n\nТекст задания: {str(list_v[n]['description'])}") 

'''Отправить ответ на задание'''
@dp.message_handler(lambda x: homework_answer(x))
async def two_custom_handler(m:Message):
    msg = m.text
    list_a =  msg.split('_$$')
    list_m = list_a[0].split('_')
    url = f"{Url_api}/add_answer"
    headers = {
        "User-Agent": User_Agent   
    }
    data={
        'first_name': f'{m.from_user.first_name}',
        'last_name': f'{m.from_user.last_name}',
        'answer': f'{list_a[1]}',
        'task_id': int(list_m[1]),
    }
    response = requests.post(url=url, headers=headers, data=data)
    if response.status_code == 200:
        print('200')
        await bot.send_message(chat_id=m.from_user.id, text = f"Ваш ответ отправлен на сервер! \n{response.status_code}")
    else:
        print(response.status_code)
        await bot.send_message(chat_id=m.from_user.id, text = f"Ошибка при отправке данных на сервер! Попробуйте позже!\nОшибка:\n{response.status_code}")
    

@dp.message_handler(lambda x: new_homework(x))
async def two_custom_handler(m:Message):
    msg = m.text
    list_m =  msg.split('_$$')
    url = f"{Url_api}/request_task"
    headers = {
        "User-Agent": User_Agent
    }
    list_m_3 = ' ' if len(list_m) < 4 else list_m[3]
    list_m_4 = ' ' if len(list_m) < 5 else list_m[4]
    data={
        'title': f'{list_m[1]}',
        'description': f'{list_m[2]}',
        'start_code': f'{list_m_3}',
        'comment': f'{list_m_4}',
    }
    response = requests.post(url=url, headers=headers, data=data)
    if response.status_code == 200:
        print('200')
        await bot.send_message(chat_id=m.from_user.id, text = f"Ваша предложка отправлена на сервер! \n{response.status_code}")
    else:
        print(response.status_code)
        await bot.send_message(chat_id=m.from_user.id, text = f"Ошибка при отправке данных на сервер! Попробуйте позже!\nОшибка:\n{response.status_code}")
    