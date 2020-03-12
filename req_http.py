import requests
import os

API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


def translate_it(text, from_lang):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    :param to_lang:
    :return:
    """

    params = {
        'key': API_KEY,
        'text': text,
        'lang': '{}-ru'.format(from_lang),
    }

    response = requests.get(URL, params=params)
    json_ = response.json()
    return ''.join(json_['text'])


if __name__ == '__main__':
    tr_f = input('Введите название файла, который необходимо перевести - без расширения, с маленькой буквы: ').upper()
    with open(f'{tr_f}.txt', encoding='utf-8-sig') as f:
        for f1 in f:
            tr = translate_it(f1, tr_f.lower())
        name_for_file = f"{tr_f}-ru.txt"
        tr_filename = os.path.join("translates", name_for_file)
        with open(tr_filename, 'w', encoding='utf-8-sig') as f2:
            f2.write(tr)