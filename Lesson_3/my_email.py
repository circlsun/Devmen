import smtplib
import os
from dotenv import load_dotenv

load_dotenv()
mail_login = os.getenv("MAIL_LOGIN")
mail_pass = os.getenv("MAIL_PASSWORD")

website = 'https://dvmn.org/referrals/ryngw37O2sVIbCI4i09Fw18Q7rD1acLYzh9uKv8B/'
friend_name = "Марк"
my_name = "Андрей"
my_email = "circlsun.matveev@yandex.ru"
friend_email = "andmatwey@yandex.ru"
subject = "Приглашение!"
сontent_type = 'text/plain; charset="UTF-8";'

letter = """\
From: {} 
To: {}
Subject: {}
Content-Type: {}

Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.
"""
letter = letter.format(my_email, friend_email, subject, сontent_type)
letter = letter.replace('%website%', website).replace('%friend_name%', friend_name).replace('%my_name%', my_name)
letter = letter.encode("UTF-8")

server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login(mail_login, mail_pass)
server.sendmail(my_email, friend_email, letter)
server.quit()


