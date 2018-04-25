
from telebot import types

import config
import telebot


bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['geophone'])
def geophone(message):
    # Эти параметры не обязательны, внедрены для удобства
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_phone = types.KeyboardButton(text="Отправить номер телефона",
                                        request_contact=True)
    button_geo = types.KeyboardButton(text="Отправить местоположение",
                                      request_location=True)
    keyboard.add(button_geo, button_phone)
    bot.send_message(message.chat.id,
                     "Отправь мне свой номер телефона или поделись местоположением!",
                     reply_markup=keyboard)


@bot.message_handler(func=lambda message: True)
def any_message(message):
    bot.reply_to(message, "Сам {}".format(message.text))


@bot.message_handler(content_types=["contact"])
def read_contact_data(message):
    if message.from_user.id == message.contact.user_id:
        # do something
        print("Same user")
    print(message.from_user.id)
    print(message.contact.user_id)
    print(message.contact.phone_number)


@bot.edited_message_handler(func=lambda message: True)
def edit_message(message):
    bot.edit_message_text(chat_id=message.chat.id,
                          text="Сам {}".format(message.text),
                          message_id=message.message_id+1)


@bot.inline_handler(func=lambda query: True)
def inline_mode(query):
    capibara1 = types.InlineQueryResultCachedPhoto(
        id='1',
        photo_file_id='AgADAgADv6gxG2V2AAFL_t69LhaAgMmmEpwOAASzOD06t4zDtlXnAwABAg',
        caption='Капибара #1'
    )
    capibara2 = types.InlineQueryResultCachedPhoto(
        id='2',
        photo_file_id='AgADAgADwKgxG2V2AAFLVUP9DHfPj3b-w0YOAAROIW_xq_gUrEyNAQABAg',
        caption='Капибара #2'
    )
    bot.answer_inline_query(query.id, [capibara1, capibara2])


if __name__ == '__main__':
    bot.polling(none_stop=True)
