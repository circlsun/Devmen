import ptbot
import os
from pytimeparse import parse
from dotenv import load_dotenv

load_dotenv()
TG_TOKEN = os.getenv('TELEG_TOKEN')
TG_CHAT_ID = os.getenv('TELEG_CHAT_ID')

def wait(chat_id, question):
    timer_s = parse(int(question))
    bot.create_timer(6, choose, author_id=chat_id, message=question)

def choose(author_id, message):
    bot.send_message(author_id, "Время вышло!")

bot = ptbot.Bot(TG_TOKEN)
bot.reply_on_message(wait)
bot.run_bot()