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

    for numSym in str(sub(r'[^\d]+', ' ', text)).strip().split():   # adding number symbols
        nlp_words.append(numSym)

    tasks = []

    # try to find from nlp_words and add ratings for words
    for idx, words in enumerate(titles):
        norm_text = str(sub(r'[^\w]', ' ', sub(r'\s+', ' ', str(words)).lower())).strip()  # TODO:: DO IT IN MYSQL!!!
        countSimilarity = [nlp_word in norm_text for nlp_word in nlp_words].count(True)

        # Если в задачи меньше слов чем в MIN_COUNT_WORDS, то данная переменная уменьшается на 1.
        if constants.MIN_COUNT_WORDS <= countSimilarity or max_count_words < constants.MIN_COUNT_WORDS and constants.MIN_COUNT_WORDS - 1 <= countSimilarity:
            tasks.append([idx, countSimilarity * constants.RATING_WORD_SIMILARITY])

    sorted_tasks = sorted(tasks, key=lambda x: x[1])

    data = []

    # adding data
    total_ratings = 0

    for idx, rating in sorted_tasks[-constants.SAMPLE_COUNT:]:
        owner_id, times = df.loc[idx, ['owner_id', 'times']]
        # space for adding params

        if user_id and owner_id == user_id:
            rating += constants.RATING_OWNER

        # END space for adding params

        total_ratings += rating
        data.append([rating, int(times)])

    # Нормализация данных для мат. ожидания
    data = stat.pv_normalize_tasks(data, total_ratings)

    # Математическое ожидание случайной величины
    mx = int(stat.math_expectation_x(data))

    # Дисперсия случайной величины
    dx = int(stat.variance_x(data, mx))

    # Среднеквадратичесвое оклонение случайной величины для задачи
    gx = int(math.sqrt(dx))

    return {'mx': display_time(mx), 'dx': display_time(dx), 'gx': display_time(gx)}
    # return {'mx': display_time(mx), 'tasks_count': len(tasks), 'data': data}


# Function for convert seconds to days, hours and minutes
intervals = (
    ('н', 604800),  # 60 * 60 * 24 * 7
    ('д', 86400),  # 60 * 60 * 24
    ('ч', 3600),  # 60 * 60
    ('м', 60),
    ('с', 1),
)


def display_time(seconds, granularity=2):
    result = []

    for name, count in intervals:
        value = seconds // count
        if value:
            seconds -= value * count
            result.append("{}{}".format(value, name))

    return ' '.join(result[:granularity])
