import os
from datetime import datetime
from pathlib import Path
from time import sleep, strptime
import requests
import json

BASE_DIR = Path(__file__).resolve().parent


def get_page(page=0):
    params = {
        'text': 'БД',
        'page': page,
        'per_page': 10
    }

    req = requests.get('https://api.hh.ru/vacancies', params)
    data = req.content.decode()
    req.close()
    return data


def get_vacancies():
    for fl in os.listdir(os.path.join(BASE_DIR, 'docs\\pagination')):
        os.remove(os.path.join(BASE_DIR, f'docs\\pagination\\{fl}'))

    for fl in os.listdir(os.path.join(BASE_DIR, 'docs\\vacancies')):
        os.remove(os.path.join(BASE_DIR, f'docs\\vacancies\\{fl}'))

    for page in range(1):
        js_obj = json.loads(get_page(page))
        next_file_name = os.path.join(BASE_DIR, './docs/pagination/{}.json'.format(
            len(os.listdir(os.path.join(BASE_DIR, 'docs\\pagination')))))

        f = open(next_file_name, mode='w', encoding='utf8')
        f.write(json.dumps(js_obj, ensure_ascii=False))
        f.close()

        if (js_obj['pages'] - page) <= 1:
            break

    print('Страницы поиска собраны')

    for fl in os.listdir(os.path.join(BASE_DIR, 'docs\\pagination')):

        # Открываем файл, читаем его содержимое, закрываем файл
        f = open(os.path.join(BASE_DIR, f'docs\\pagination\\{fl}'), encoding='utf8')
        json_text = f.read()
        f.close()

        # Преобразуем полученный текст в объект справочника
        json_obj = json.loads(json_text)

        # Получаем и проходимся по непосредственно списку вакансий
        for v in json_obj['items']:
            # Обращаемся к API и получаем детальную информацию по конкретной вакансии
            req = requests.get(v['url'])
            data = req.content.decode()
            req.close()

            # Создаем файл в формате json с идентификатором вакансии в качестве названия
            # Записываем в него ответ запроса и закрываем файл
            file_name = os.path.join(BASE_DIR, f'docs\\vacancies\\{v["id"]}')
            f = open(file_name, mode='w', encoding='utf8')
            f.write(data)
            f.close()
            sleep(0.25)

    print('Вакансии собраны')

    vacancies = []

    for fl in os.listdir(os.path.join(BASE_DIR, 'docs\\vacancies')):
        f = open((os.path.join(BASE_DIR, f'docs\\vacancies\\{fl}')), encoding='utf8')
        json_text = f.read()
        f.close()
        json_obj = json.loads(json_text)
        salary = f'{json_obj["salary"]["from"]} - {json_obj["salary"]["to"]}' if json_obj['salary'] else "Не указана"
        salary = salary.replace('None', '')
        currency = f"{json_obj['salary']['currency']}" if json_obj['salary'] else ''
        PATTERN_IN = "%Y-%m-%dT%H:%M:%S+0300"
        PATTERN_OUT = "%Y.%m.%d %H:%M"
        json_obj['published_at'] = datetime.strptime(json_obj['published_at'], PATTERN_IN)
        json_obj['published_at'] = datetime.strftime(json_obj['published_at'], PATTERN_OUT)
        skills = []
        for skill in json_obj['key_skills']:
            for key, value in skill.items():
                skills.append(value)

        vacancies.append([json_obj['name'], json_obj['description'], skills,
                          json_obj['employer']['name'], salary, json_obj['area']['name'],
                          json_obj['published_at'], currency])

    return vacancies
