import os
import telebot as t
from datetime import datetime
import time
from telebot.types import Message as m
dd=os.path.join(os.path.dirname(__file__))
bot = t.telebot.TeleBot(token='7992565364:AAE1dXHxjYWgr6wbUwW7DPP3WcPVloBC4g8')
@bot.message_handler(['time'])
def OTKAT(message:m):
    forum=datetime.today().strftime('%Y/%m/%d %H:%M:%S')
    bot.send_message(message.chat.id,forum)
@bot.message_handler(['id'])
def idi(message:m):
    bot.send_message(message.chat.id,f'{message.chat.id}')
bot.infinity_polling()