
from telebot import types

import config
import telebot
from time import time


bot = telebot.TeleBot(config.token)


def get_language(lang_code):
    # Иногда language_code может быть None
    if not lang_code:
        return "en"
    if '-' in lang_code:
        lang_code = lang_code.split('-')[0]
    if lang_code == 'ru':
        return "ru"
    else:
        return "en"


restricted_messages = ["че по дедлайнам?, мы в дерьме...", "i am vegan"]
#  and message.chat.id == config.GROUP_ID


# Выдаём Read-only за определённые фразы
@bot.message_handler(func=lambda message: message.text and message.text.lower() in restricted_messages)
def set_ro(message):
    bot.restrict_chat_member(message.chat.id, message.from_user.id, until_date=time()+600)
    bot.send_message(message.chat.id, "Вам запрещено отправлять сюда сообщения в течение 10 минут. Вы слишком горите!",
                     reply_to_message_id=message.message_id)


if __name__ == '__main__':
    bot.polling(none_stop=True)


