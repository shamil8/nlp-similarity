# рейтинг задач максимально "неправильных"
import pandas as pd


df = pd.read_csv('/app/data/all_tasks.csv', header=None, names=['names'])

main_words = [
    'моделирование',
    'оформление',
    'спецификация',
    'подсчет',
    'расчет',
    'анализ',
    'разработка',
    'проверка',
    'создание',
    'корректировка',
    'исправление',

    # verbs
    'моделировать',
    'оформлять',
    'посчитать',
    'рассчитать',
    'анализировать',
    'разработать',
    'проверить'
    'создать',
    'корректировать',
    'исправить',
]

names = df['names'].str.lower()


def get_rating_tasks():
    result = []

    for name in names:
        txt = name.split()
        rating = 0

        for words in names:
            for idx, word in enumerate(str(words).split()):
                if idx == 0 and word in txt and txt in main_words:
                    rating += 2000
                elif word in txt:
                    rating += 1

        result.append([name, rating])

    result.sort(key=sort_second)

    return result


def sort_second(val):
    return val[1]
