import file_operations
from faker import Faker
import random 
import os


MIN_RANGE = 3
MAX_RANGE = 18
QUANTITY = 10


def create_runic_skills():
    skills = [
    'Стремительный прыжок', 
    'Электрический выстрел',
    'Ледяной удар', 
    'Стремительный удар', 
    'Кислотный взгляд',
    'Тайный побег', 
    'Ледяной выстрел',
    'Огненный заряд',
   ]
    letters_mapping = {
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
    ' ': ' ',
   }
    runic_skills = []
    for skill in skills:
        for char in skill:
            skill = skill.replace(
            char, letters_mapping[char])
        runic_skills.append(skill)
    return runic_skills


def create_completed_templates(MIN_RANGE, MAX_RANGE):
    fake = Faker('ru_RU')
    runic_skill1, runic_skill2, runic_skill3 = (
    random.sample(create_runic_skills(), 3)
    )
    context = {
       'first_name': fake.first_name(),
       'last_name': fake.last_name(),
       'job': fake.job(),
       'town': fake.city(),
       'strength': random.randint(MIN_RANGE, MAX_RANGE),
       'agility': random.randint(MIN_RANGE, MAX_RANGE),
       'endurance': random.randint(MIN_RANGE, MAX_RANGE),
       'intelligence': random.randint(MIN_RANGE, MAX_RANGE),
       'luck': random.randint(MIN_RANGE, MAX_RANGE),
       'skill_1':(runic_skill1),
       'skill_2':(runic_skill2),
       'skill_3':(runic_skill3),
    }
    return context


def main(QUANTITY):
    if not os.path.exists('test_dir'):
       os.makedirs('test_dir')
    for complited_templates in range(QUANTITY):
        file_operations.render_template(
             'charsheet.svg',
             f'test_dir/result{complited_templates}.svg',
             create_completed_templates(MIN_RANGE, MAX_RANGE))
   


if __name__ == '__main__':
    main(QUANTITY)