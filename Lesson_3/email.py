pattern = """Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

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
website = 'https://dvmn.org/referrals/ryngw37O2sVIbCI4i09Fw18Q7rD1acLYzh9uKv8B/'
friend_name = "Марк"
my_name = "Андрей"
my_email = "circlsun.matveev@yandex.ru"
friend_email = "petr@yandex.ru"
subject = "Приглашение!"
h1_сontent_type = 'text/plain'
h2_сontent_type = "UTF-8"

# From: ivan@yandex.ru
# To: petr@yandex.ru
# Subject: Приглашение!
# Content-Type: text/plain; charset="UTF-8";

mail_title = (f"From: {my_email}\n" 
              f"To: {friend_email}\n"
              f"Subject: {subject}\n"
              f"Content-Type: {h1_сontent_type}; {h2_сontent_type};"
)
letter = pattern.replace('%website%', website).replace('%friend_name%', friend_name).replace('%my_name%', my_name)

#print(mail_title)
#print()
print(mail_title, letter, sep='\n\n')


