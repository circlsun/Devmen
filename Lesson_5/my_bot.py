import ptbot
import os
from pytimeparse import parse
from dotenv import load_dotenv

load_dotenv()
TG_TOKEN = os.getenv('TELEG_TOKEN')
TG_CHAT_ID = os.getenv('TELEG_CHAT_ID')

def main():

    def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
        iteration = min(total, iteration)
        percent = "{0:.1f}"
        percent = percent.format(100 * (iteration / float(total)))
        filled_length = int(length * iteration // total)
        pbar = fill * filled_length + zfill * (length - filled_length)
        return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)

    def reply(chat_id, text):
        timer_s = parse(text)
        message_id = bot.send_message(chat_id, "Запускаю таймер!")
        bot.create_countdown(timer_s, notify, msg_id=message_id, author_id=chat_id, timer=timer_s)
        bot.create_timer(timer_s, set_end, author_id=chat_id)
       
    def set_end(author_id):
        bot.send_message(author_id, 'Время вышло!')
    
    def notify(secs_left, author_id, msg_id, timer):
      message = f"Осталось {secs_left} секунд!\n{render_progressbar(timer, secs_left)}"
      bot.update_message(author_id, msg_id,  message)
          
    bot = ptbot.Bot(TG_TOKEN)
    bot.reply_on_message(reply)
    bot.run_bot()


if __name__ == '__main__':
    main()
