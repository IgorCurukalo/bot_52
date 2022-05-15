from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

kb1 = InlineKeyboardMarkup(row_width=1)
pars = [['1. Узнавать появилось ли новое задание',1], ['2. Получать текст задания (по id)',2],
['3. Отправлять ответ на задание',3],['4. Отправлять задания в предложку',4]]
kb1.add(*[InlineKeyboardButton(i, callback_data=f'para-{j}') for i, j in pars])


