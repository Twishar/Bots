
import telebot
import BotAPIv2.config as config

bot = telebot.TeleBot(config.token)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    bot.send_message(message.from_user.id, """\r
    <b>Bold / Жирное</b> форматирование
    <i>Italic / Наклоное</i> форматирование
    <code>inline fixed-width code</code>
    <pre>
        pre-formatted fixed-width code block
        if you.can_read(code)==True:
            bot.send_message(id, "U are ...")
    </pre>
    <a href="URL">
        https://www.youtube.com/watch?v=09buxer2r-I
    </a>
    """, parse_mode="HTML")


bot.polling(none_stop=True)
