import smtplib

# letter = """\
# From: circlsun.matveev@yandex.ru
# To: andmatwey@yandex.ru
# Subject: Важно!
# Content-Type: text/plain; charset="UTF-8";

# YOHOOO!"""

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

Привет, """

letter = letter.format(my_email, friend_email, subject, сontent_type)
letter = letter.replace('%website%', website).replace('%friend_name%', friend_name).replace('%my_name%', my_name)
letter = letter.encode("UTF-8")

server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login('circlsun.matveev', 'chfetuqwxmljzhrf')
server.sendmail('circlsun.matveev@yandex.ru', 'andmatwey@yandex.ru', letter)
server.quit()
