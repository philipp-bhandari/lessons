import requests
import os
from urllib.parse import quote

API = 'trnsl.1.1.20181205T154221Z.04af06a37492936a.d96e3ff5f700d19ff36d1fa1c76ca88c3681d6c4'
detect_url = 'https://translate.yandex.net/api/v1.5/tr.json/detect'
translate_url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
texts = 'texts'


def generator(x: int):
    while True:
        x += 1
        yield x


def detect_lang(url, api, text):
    url = f'{url}?key={api}&text={text}'
    response = requests.get(url)
    lang = response.json()
    return lang['lang']


def translate(path_to_file, url_detect, url_translate, api):
    with open(path_to_file) as file:
        file_content = quote(file.read())
    lang = detect_lang(url_detect, api, file_content)

    params = f'key={api}&text={file_content}&lang={lang}-ru&'
    response = requests.post(url_translate, params=params)
    body = response.json()
    return body['text'][0]


if __name__ == '__main__':
    try:
        texts_directory = os.path.join(os.getcwd(), texts)
        text_files = os.listdir(texts_directory)
        file_counter = generator(0)
        files_path_dict = {}

        if len(text_files) != 0:
            print('\nНиже список файлов. Выберите какой нужно перевести. Для этого введите соответствующий ему номер.')

            for file in text_files:
                file_path = os.path.join(texts_directory, file)
                if os.path.isfile(file_path):
                    counter = file_counter.__next__()
                    files_path_dict[counter] = file_path
                    print(f'{counter}: {file}')

            try:
                number = int(input())
                if number not in files_path_dict.keys():
                    print('\nФайл с таким номером не найден.')
                else:
                    result = translate(files_path_dict[number], detect_url, translate_url, API)
                    translated_doc = os.path.join(texts_directory, 'RU')
                    with open(translated_doc, 'w') as file:
                        file.write(result)
                    print(f'Результат записан в файл: {translated_doc}')
                    print('\n', result)
            except ValueError:
                print('\nВ следующий раз введите корректный номер файла.')
        else:
            print(f'\nВ папке {texts} нет файлов. Для перевода поместите файлы в папку.')
    except FileNotFoundError:
        print(f'\nПапка {texts} должна быть в папке со скриптом, в данный момент папка не обнаружена.')










