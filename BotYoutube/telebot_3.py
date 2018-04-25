import os
import telebot
import config
import random
import urllib.request as urlib2

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('/start', '/stop')
    user_markup.row('фото', 'аудио', 'документы')
    user_markup.row('стикер', 'видео', 'голос', 'локация')
    bot.send_message(message.from_user.id, 'Добро пожаловать..', reply_markup=user_markup)


@bot.message_handler(commands=['stop'])
def handle_start(message):
    hide_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id, '..', reply_markup=hide_markup)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == 'фото':
        # all_files_in_directory = os.listdir(config.py.photo_directory)
        # random_file = random.choice(all_files_in_directory)
        url = 'https://goo.gl/58RCFF'
        urlib2.urlretrieve(url, 'url_image.jpg')
        img = open('url_image.jpg', 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()

    elif message.text == 'аудио':
        audio = open(config.music_directory + '/' + 'disturbed-the-light-immortalized-2015.mp3', 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_audio')
        bot.send_audio(message.from_user.id, audio)
        audio.close()

    elif message.text == 'документы':
        directory = config.files_directory
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)

        for file in all_files_in_directory:
            document = open(directory + '/' + file, 'rb')
            bot.send_chat_action(message.from_user.id, 'upload_document')
            bot.send_document(message.from_user.id, document)
            document.close()

    elif message.text == 'стикер':
        bot.send_sticker(message.from_user.id, config.template_sticker_id)

    elif message.text == 'видео':
        video = open(config.video_directory + '/' + 'id_Video', 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_video')
        bot.send_video(message.from_user.id, video)
        video.close()

    elif message.text == 'голос':
        # В формате ogg
        voice = open(config.voice_directory + '/' + 'voice_id', 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_audio')
        bot.send_voice(message.from_user.id, voice)
        voice.close()

    elif message.text == 'локация':
        bot.send_chat_action(message.from_user.id, 'find_location')
        bot.send_location(message.from_user.id, 54.5175971, 42.9631043)


bot.polling(none_stop=True)
