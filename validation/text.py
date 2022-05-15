from main import bot, dp #, anti_flood
from aiogram.types import Message
from config import admin_id
# from tools.parser import pars_www

def return_homework_id(message: Message) -> bool:
    msg = message.text
    list_m = msg.split('_')
    return list_m[0] == 'id' and int(list_m[1]) > 0 and len(list_m) < 3

def homework_answer(message: Message) -> bool:
    msg = message.text
    list_a =  msg.split('_$$')
    list_m = list_a[0].split('_')
    return list_m[0] == 'id' and int(list_m[1]) > 0 and len(list_m) < 3 and len(list_a[1]) > 1

def new_homework(message: Message) -> bool:
    msg = message.text
    list_m =  msg.split('_$$')
    print(list_m)
    print(len(list_m))
    return list_m[0] == 'new' and list_m[1] != ''  and list_m[2] != '' and len(list_m) < 6


def is_admin(m: Message):
    return m.from_user.id == admin_id

