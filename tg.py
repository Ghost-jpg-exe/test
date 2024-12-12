import os
import telebot as t
from telebot.types import Message as m
dd=os.path.join(os.path.dirname(__file__))
bot = t.telebot.TeleBot(token='7992565364:AAE1dXHxjYWgr6wbUwW7DPP3WcPVloBC4g8')
bot.infinity_polling()