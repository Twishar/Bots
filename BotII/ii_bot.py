import config
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler
import apiai
import json


updater = Updater(token=config.token)
dispatcher = updater.dispatcher


def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Дарова')


def textMessage(bot, update):
    request = apiai.ApiAI(config.flow_token).text_request()  # Токен API к DialogFlow
    request.lang = 'ru'  # На каком языке будет послан запрос
    request.session_id = 'TestApiBot'
    request.query = update.message.text   # Посылаем запрос к ИИ с сообщением от юзера

    responseJson = json.loads(request.getresponse().read().decode('utf-8'))
    response = responseJson['result']['fulfillment']['speech']      # Разбираем JSON и вытаскиваем ответ

    # Если есть ответ от бота - присылаем юзеру, если нет - бот его не понял
    if response:
        bot.send_message(chat_id=update.message.chat_id, text=response)
    else:
        bot.send_message(chat_id=update.message.chat_id, text='Я вас не совсем понял!')


# Хендлеры
start_command_handler = CommandHandler('start', startCommand)
text_message_handler = MessageHandler(Filters.text, textMessage)

# Добавляем хендлеры в диспетчер
dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)

# Начинаем поиск обновлений
updater.start_polling(clean=True)

updater.idle()
