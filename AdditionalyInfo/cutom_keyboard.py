import telebot
from telebot import types

bot = telebot.TeleBot("u token")

markup = types.ReplyKeyboardMarkup()
markup.row('a', 'v')
markup.row('c', 'd', 'e')
# bot.send_message(message.chat.id, "Choose one letter", reply_markup=markup)
"""В одной из функций, при приеме сообщения от пользователя"""
