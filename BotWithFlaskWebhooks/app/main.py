import config
import requests
import re
from flask import Flask, request, jsonify
from flask_sslify import SSLify

app = Flask(__name__)
sslify = SSLify(app)

# Very nice video for webhooks https://www.youtube.com/watch?v=Al7hkU6RO9M

token = config.token
URL = 'https://api.telegram.org/bot{}/'.format(config.token)


def send_message(chat_id, text='some text'):
    url = URL + 'sendMessage'
    answer = {'chat_id': chat_id,
              'text': text}
    r = requests.post(url, json=answer)
    return r.json()


def parse_text(text):
    pattern = r'/\w+'
    crypto = re.search(pattern, text).group()
    return crypto[1:]


def get_price(crypto):
    url = 'https://api.coinmarketcap.com/v1/ticker/{}'.format(crypto)
    r = requests.get(url).json()
    price = r[-1]['price_usd']
    return price


@app.route('/{}'.format(config.token), methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        r = request.get_json()
        chat_id = r['message']['chat']['id']
        message = r['message']['text']

        pattern = r'/\w+'

        if re.search(pattern, message):
            price = get_price(parse_text(message))
            send_message(chat_id, text=price)

        return jsonify(r)

    return '<h1>Bot welcomes you</h1>'


if __name__ == '__main__':
    app.run()
