from random import choice
import requests

from basic_word import BasicWord


def load_random_word(link):
    """Функция переходит по ссылке, выбирает оттуда рандомно один словарь из списка словарей,
        с помощью которого создает экземпляр класса BasicWord и возвращает его """
    value = requests.get(f'{link}b/JQCA').json()
    random_choice_dict = choice(value)
    word = random_choice_dict.get('word')
    word_array = random_choice_dict.get('subwords')
    # print(word, word_array)
    if __name__ == "__main__":
        vvod1 = str(input('Введите ваше имя'))
        print(f'Привет {vvod1}')
        vvod = str(input(f'Введите слова не короче 3 букв от слова {word} или стоп, чтобы прервать, на самом деле, будут подсказки'))
        val = word_array
        print(len(val))
        while len(val) > 1 or vvod == "стоп":
            if vvod not in val:
                print(f'Такого слова нет подсказка: {word_array}')
            val.remove(vvod)

            vvod = str(input(f'Введите слова от слова {word} или стоп, чтобы прервать'))
            print(word_array, len(word_array))
            if len(val) == 1:
                print('Finish')

    # exemplar = BasicWord(word, word_array)
    # return exemplar
load_random_word('https://www.jsonkeeper.com/')