import random
import file_operations
from faker import Faker

min_point, max_point = 3, 18
number_cards = 10
alpha = {
    'а': 'а͠',
    'б': 'б̋',
    'в': 'в͒͠',
    'г': 'г͒͠',
    'д': 'д̋',
    'е': 'е͠',
    'ё': 'ё͒͠',
    'ж': 'ж͒',
    'з': 'з̋̋͠',
    'и': 'и',
    'й': 'й͒͠',
    'к': 'к̋̋',
    'л': 'л̋͠',
    'м': 'м͒͠',
    'н': 'н͒',
    'о': 'о̋',
    'п': 'п̋͠',
    'р': 'р̋͠',
    'с': 'с͒',
    'т': 'т͒',
    'у': 'у͒͠',
    'ф': 'ф̋̋͠',
    'х': 'х͒͠',
    'ц': 'ц̋',
    'ч': 'ч̋͠',
    'ш': 'ш͒͠',
    'щ': 'щ̋',
    'ъ': 'ъ̋͠',
    'ы': 'ы̋͠',
    'ь': 'ь̋',
    'э': 'э͒͠͠',
    'ю': 'ю̋͠',
    'я': 'я̋',
    'А': 'А͠',
    'Б': 'Б̋',
    'В': 'В͒͠',
    'Г': 'Г͒͠',
    'Д': 'Д̋',
    'Е': 'Е',
    'Ё': 'Ё͒͠',
    'Ж': 'Ж͒',
    'З': 'З̋̋͠',
    'И': 'И',
    'Й': 'Й͒͠',
    'К': 'К̋̋',
    'Л': 'Л̋͠',
    'М': 'М͒͠',
    'Н': 'Н͒',
    'О': 'О̋',
    'П': 'П̋͠',
    'Р': 'Р̋͠',
    'С': 'С͒',
    'Т': 'Т͒',
    'У': 'У͒͠',
    'Ф': 'Ф̋̋͠',
    'Х': 'Х͒͠',
    'Ц': 'Ц̋',
    'Ч': 'Ч̋͠',
    'Ш': 'Ш͒͠',
    'Щ': 'Щ̋',
    'Ъ': 'Ъ̋͠',
    'Ы': 'Ы̋͠',
    'Ь': 'Ь̋',
    'Э': 'Э͒͠͠',
    'Ю': 'Ю̋͠',
    'Я': 'Я̋',
    ' ': ' '
}
skills = [
    "Стремительный прыжок",
    "Электрический выстрел",
    "Ледяной удар",
    "Стремительный удар",
    "Кислотный взгляд",
    "Тайный побег",
    "Ледяной выстрел",
    "Огненный заряд",
]
SRC = "/Users/admin/VSCode/Devmen/Lesson_6/src/charsheet.svg"
RES = "/Users/admin/VSCode/Devmen/Lesson_6/output/result_{}.svg"


def get_string(_list):
    return ''.join(_list)


def get_skills(runic_skills):
    temporal = []
    for skill in random.sample(skills, 3):
        for char in skill:
            temporal.append(alpha[char])
        runic_skills.append(get_string(temporal))
        temporal = []
    return runic_skills


def get_content():
    context = {}
    runic_skills = []
    fake = Faker("ru_RU")
    context["first_name"] = fake.first_name_male()
    context["last_name"] = fake.last_name_male()
    context["job"] = fake.job()
    context["town"] = fake.city()
    context["strength"] = random.randint(min_point, max_point)
    context["agility"] = random.randint(min_point, max_point)
    context["endurance"] = random.randint(min_point, max_point)
    context["intelligence"] = random.randint(min_point, max_point)
    context["luck"] = random.randint(min_point, max_point)
    context["skill_1"] = get_skills(runic_skills)[0]
    context["skill_2"] = get_skills(runic_skills)[1]
    context["skill_3"] = get_skills(runic_skills)[2]
    return context


def get_cards():
    for name in range(1, number_cards + 1):
        runic_skills = []
        get_skills(runic_skills)
        file_operations.render_template(SRC, RES.format(name), get_content())


def main():
    get_cards()


if __name__ == "__main__":
    main()
