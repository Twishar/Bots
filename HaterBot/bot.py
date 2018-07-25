
import telebot
import config
import json


bot = telebot.TeleBot(config.telegram_token)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Ну Дарова, чем я обязан такому почтению?')


@bot.message_handler(commands=['stop'])
def stop(message):
    bot.reply_to(message, "А вот и не угадал, у тебя нет здесь власти")


@bot.message_handler()
def any_message(message):
    bot.send_message(message.chat.id, 'Ку')


if __name__ == '__main__':
    bot.polling(none_stop=True)
