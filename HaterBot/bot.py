
import time
import json
import pyowm
import flask
import apiai
import config
import telebot
import requests
import messages
from flask import Flask
from flask_sslify import SSLify


bot = telebot.TeleBot(config.telegram_token)
app = Flask(__name__)
sslify = SSLify(app)
WEBHOOK_URL_PATH = "/{}/".format(config.telegram_token)
WEBHOOK_URL_BASE = config.base_url_webhook


@app.route('/', methods=['GET', 'HEAD'])
def index():
    return ''


# Process webhook calls
@app.route(WEBHOOK_URL_PATH, methods=['POST'])
def webhook():
    if flask.request.headers.get('content-type') == 'application/json':
        json_string = flask.request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''
    else:
        flask.abort(403)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, messages.start)


@bot.message_handler(commands=['stop'])
def stop(message):
    bot.reply_to(message, messages.stop)


@bot.message_handler(commands=['weather'])
def give_forecast(message):
    owm = pyowm.OWM(config.open_weather_map_token)
    obs = owm.weather_at_place('Kyiv,UA')
    w = obs.get_weather()
    text = "Статус по погоде: {}\n" \
           "Влажность: {}\n" \
           "Температура: {}\n" \
           "Ветер: {}\n" \
           "Расширенный статус: {}".format(w.get_status(), w.get_humidity(), w.get_temperature('celsius'),
                                           w.get_wind(), w.get_detailed_status())
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['curs'])
def currency_curs(message):
    url = 'http://bank-ua.com/export/exchange_rate_cash.json'
    response_json = requests.get(url)
    usd = response_json.json()[-2]
    eur = response_json.json()[-3]
    text = "Курс валют по Привату:\n" \
           "USD:  Покупка: {}  ||  Продажа: {}\n" \
           "EUR:  Покупка: {}  ||  Продажа: {}".format(usd['rateBuy'], usd['rateSale'],
                                                       eur['rateBuy'], eur['rateSale'])

    bot.send_message(message.chat.id, text)


"""
В доработке
@bot.message_handler()
def any_message(message):
    request = apiai.ApiAI(config.dialog_flow_token).text_request()
    request.lang = 'ru'  # На каком языке будет послан запрос
    request.session_id = messages.session_id
    request.query = message.text    # Посылаем запрос к ИИ с сообщением юзера
    response_json = json.loads(request.getresponse().read().decode('utf-8'))
    response = response_json['result']['fulfillment']['speech']

    if response:
        bot.send_message(chat_id=message.chat.id, text=response)
    else:
        bot.send_message(chat_id=message.chat.id, text=messages.default_answer)
"""


# Remove webhook, it fails sometimes the set if there is a previous webhook
bot.remove_webhook()

time.sleep(0.1)

# Set webhook
bot.set_webhook(url=WEBHOOK_URL_BASE+WEBHOOK_URL_PATH)


if __name__ == '__main__':
    app.run()
