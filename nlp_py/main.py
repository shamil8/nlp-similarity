import math
import pandas as pd
import nlp_py.constants as constants
from nlp_py.similarity import get_similarity
from nlp_py import stat
from re import sub

df = pd.read_csv('/app/data/tasks-from-mover.csv')
titles = df['name'].str.lower()


def get_similarity_date(text, user_id=None):
    max_count_words = len(text.split())
    text_nlp = str(sub(r'[^\w]|[^\D]', ' ', text).lower()).strip()  # TODO:: MAYBE CHANGE IT after MYSQL!!!
    nlp_words = get_similarity(text_nlp, True)

    for numSym in str(sub(r'[^\d]+', ' ', text)).strip().split():  # adding number symbols
        nlp_words.append(numSym)

    tasks = []

    # try to find from nlp_words and add ratings for words
    for idx, words in enumerate(titles):
        norm_text = str(sub(r'[^\w]', ' ', sub(r'\s+', ' ', str(words)).lower())).strip()  # TODO:: DO IT IN MYSQL!!!
        countSimilarity = [nlp_word in norm_text for nlp_word in nlp_words].count(True)

        # Если в задачи меньше слов чем в MIN_COUNT_WORDS, то данная переменная уменьшается на 1.
        if constants.MIN_COUNT_WORDS <= countSimilarity or max_count_words < constants.MIN_COUNT_WORDS and constants.MIN_COUNT_WORDS - 1 <= countSimilarity:
            tasks.append([idx, countSimilarity ** constants.RATING_WORD_SIMILARITY])

    sorted_tasks = sorted(tasks, key=lambda x: x[1])
    tasks = sorted_tasks[-constants.SAMPLE_COUNT:]
    data = []

    # adding data
    total_ratings = 0
    min_rating = tasks[0][0]

    for idx, rating in tasks:
        owner_id, times = df.loc[idx, ['owner_id', 'times']]

        if not times:
            continue
        # space for adding some params

        if user_id and owner_id == user_id:
            rating += constants.RATING_OWNER

        # END space for adding some params
        if rating < min_rating:
            min_rating = rating

        total_ratings += rating
        data.append([rating, int(times / 60), idx])  # TODO:: Convert times to minute in MySQL

    sorted_data = sorted(data, key=lambda x: x[1])

    # Удаляем из выборки данные разность которых больше чем constants.DELTA_DIFFERENT
    i = 0
    while i < len(sorted_data):
        if sorted_data[len(sorted_data) - (i + 1)][1] - sorted_data[i][1] < constants.DELTA_DIFFERENT:
            break

        # removing useless data
        if min_rating == sorted_data[i][0]:
            total_ratings -= sorted_data[i][0]
            del sorted_data[i]
        if min_rating == sorted_data[len(sorted_data) - (i + 1)][0]:
            total_ratings -= sorted_data[len(sorted_data) - (i + 1)][0]
            del sorted_data[len(sorted_data) - (i + 1)]

        i += 1

    # Нормализация данных для мат. ожидания
    data = stat.pv_normalize_tasks(sorted_data, total_ratings)

    # Математическое ожидание случайной величины
    mx = int(stat.math_expectation_x(data))

    # Дисперсия случайной величины
    dx = int(stat.variance_x(data, mx))

    # Среднеквадратичесвое оклонение случайной величины для задачи
    gx = int(math.sqrt(dx))

    return {
        'mx': display_time(mx),
        'dx': display_time(dx),
        'gx': display_time(gx),
        'min_data': {
            'name': df.loc[sorted_data[-1][2], 'name'],
            'rating': sorted_data[0][0],
            'time': sorted_data[0][1],
        },
        'max_data': {
            'name': df.loc[sorted_data[-1][2], 'name'],
            'rating': sorted_data[-1][0],
            'time': sorted_data[-1][1],
        }
    }
    # return {'mx': display_time(mx), 'tasks_count': len(tasks), 'data': data}


# Function for convert seconds to days, hours and minutes
intervals = (
    ('н', 10080),  # 60 * 24 * 7
    ('д', 1440),  # 60 * 24
    ('ч', 60),  # 60
    ('м', 1),
)


def display_time(seconds, granularity=2):
    result = []

    for name, count in intervals:
        value = seconds // count
        if value:
            seconds -= value * count
            result.append("{}{}".format(value, name))

    return ' '.join(result[:granularity])
