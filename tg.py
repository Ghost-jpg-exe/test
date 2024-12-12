import os
import telebot as t
import time
from datetime import datetime
from telebot.types import Message as m
dd=os.path.join(os.path.dirname(__file__))
bot = t.telebot.TeleBot(token='7992565364:AAE1dXHxjYWgr6wbUwW7DPP3WcPVloBC4g8')
@bot.message_handler(['time'])
def OTKAT(message:m):
    forum=datetime.today().strftime('%Y/%m/%d %H:%M:%S')
    bot.send_message(message.chat.id,forum)
bot.infinity_polling()