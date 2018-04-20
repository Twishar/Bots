import config
import telegram

bot = telegram.Bot(token=config.token)
print(bot.get_me())
