import config
import telebot

from datetime import datetime


bot = telebot.TeleBot(config.token)

# bot.send_message('381331119', 'test')

# upd = bot.get_updates()
# print(upd)

# last_upd = upd[-1]
# message_from_user = last_upd.message
# print(message_from_user)

print(bot.get_me())


def log(message, answer):
    print('\n -------')
    print(datetime.now())
    print("Сообщение от {} {}. (id = {}) \n Текст - {}".format(message.from_user.first_name,
                                                               message.from_user.last_name,
                                                               str(message.from_user.id),
                                                               message.text))
    print(answer)


@bot.message_handler(commands=['help'])
def handle_text(message):
    bot.send_message(message.chat.id, 'иЗИ БОт')


@bot.message_handler(content_types=['text'])
def handle_text(message):
    answer = 'ПРоигрыш'
    if message.text == 'а':
        answer = 'Б'
        log(message, answer)
        bot.send_message(message.chat.id, answer)
    elif message.text == 'б':
        answer = 'В'
        log(message, answer)
        bot.send_message(message.chat.id, answer)
    else:
        log(message, answer)
        bot.send_message(message.chat.id, answer)


bot.polling(none_stop=True, interval=0)
