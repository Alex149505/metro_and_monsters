from file_operations import VERSION
import file_operations
from faker import Faker
import random 
import os
fake = Faker("ru_RU")
min_range = 3
max_range = 18
quantity = 10
skills = ["Стремительный прыжок", 
          "Электрический выстрел",
          "Ледяной удар", 
          "Стремительный удар", 
          "Кислотный взгляд",
          "Тайный побег", 
          "Ледяной выстрел",
          "Огненный заряд"
]
letters_mapping = {
    'а': 'а͠', 'б': 'б̋', 'в': 'в͒͠',
    'г': 'г͒͠', 'д': 'д̋', 'е': 'е͠',
    'ё': 'ё͒͠', 'ж': 'ж͒', 'з': 'з̋̋͠',
    'и': 'и', 'й': 'й͒͠', 'к': 'к̋̋',
    'л': 'л̋͠', 'м': 'м͒͠', 'н': 'н͒',
    'о': 'о̋', 'п': 'п̋͠', 'р': 'р̋͠',
    'с': 'с͒', 'т': 'т͒', 'у': 'у͒͠',
    'ф': 'ф̋̋͠', 'х': 'х͒͠', 'ц': 'ц̋',
    'ч': 'ч̋͠', 'ш': 'ш͒͠', 'щ': 'щ̋',
    'ъ': 'ъ̋͠', 'ы': 'ы̋͠', 'ь': 'ь̋',
    'э': 'э͒͠͠', 'ю': 'ю̋͠', 'я': 'я̋',
    'А': 'А͠', 'Б': 'Б̋', 'В': 'В͒͠',
    'Г': 'Г͒͠', 'Д': 'Д̋', 'Е': 'Е',
    'Ё': 'Ё͒͠', 'Ж': 'Ж͒', 'З': 'З̋̋͠',
    'И': 'И', 'Й': 'Й͒͠', 'К': 'К̋̋',
    'Л': 'Л̋͠', 'М': 'М͒͠', 'Н': 'Н͒',
    'О': 'О̋', 'П': 'П̋͠', 'Р': 'Р̋͠',
    'С': 'С͒', 'Т': 'Т͒', 'У': 'У͒͠',
    'Ф': 'Ф̋̋͠', 'Х': 'Х͒͠', 'Ц': 'Ц̋',
    'Ч': 'Ч̋͠', 'Ш': 'Ш͒͠', 'Щ': 'Щ̋',
    'Ъ': 'Ъ̋͠', 'Ы': 'Ы̋͠', 'Ь': 'Ь̋',
    'Э': 'Э͒͠͠', 'Ю': 'Ю̋͠', 'Я': 'Я̋',
    ' ': ' '
}


def create_runic_skills(skills):
    runic_skills = []
    for skill in skills:
        for char in skill:
            skill = skill.replace(char, letters_mapping[char])
        runic_skills.append(skill)
    return runic_skills


def create_completed_templates(min_range, max_range):
    runic_skill = random.sample(create_runic_skills(skills), 3)
    
    context = {
       "first_name": fake.first_name(),
       "last_name": fake.last_name(),
       "job": fake.job(),
       "town": fake.city(),
       "strength": random.randint(min_range, max_range),
       "agility": random.randint(min_range, max_range),
       "endurance": random.randint(min_range, max_range),
       "intelligence": random.randint(min_range, max_range),
       "luck": random.randint(min_range, max_range),
       "skill_1": (runic_skill [0]),
       "skill_2": (runic_skill [1]),
       "skill_3": (runic_skill [2])
    }
    return context


def render_templates(quantity):
    if not os.path.exists('/metro_and_monsters/test_dir'):
       os.makedirs('/metro_and_monsters/test_dir')
    for complited_templates in range(quantity):
        file_operations.render_template(
             'charsheet.svg',
             f'/metro_and_monsters/test_dir/result{complited_templates}.svg',
            create_completed_templates(min_range, max_range))
   

def main():
    render_templates(quantity)


if __name__ == "__main__":
    main()