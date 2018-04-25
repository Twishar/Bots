
from telebot import types

import config
import telebot

GROUP_ID = -100124312982  # для примера, это рандомный набор цифр

bot = telebot.TeleBot(config.token)


@bot.message_handler(func=lambda message: message.entities is not None and message.chat.id == GROUP_ID)
def delete_links(message):
    for entity in message.entities:     # Пройдемся по всем entities в поисках ссылок
        # url - обычная ссылка, text_link - ссылка, скрытая под текстом
        if entity.type in ["url", "text_link"]:
            # Мы можем не проверять chat.id, он проверяется еще в хендлере
            bot.delete_message(message.chat.id, message.message_id)
        else:
            return


if __name__ == '__main__':
    bot.polling(none_stop=True)
