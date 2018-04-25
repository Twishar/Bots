
import telebot

bot = telebot.TeleBot('some token')


@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    pass


@bot.message_handler(content_types=['document', 'audio'])
def handle_docs_audio(message):
    pass


@bot.message_handler(regexp="Some Regexp")
def handle_message(message):
    pass


@bot.message_handler(func=lambda message: message.document.mime_type == 'text/plain',
                     content_types=['document'])
def handle_text_doc(message):
    pass

