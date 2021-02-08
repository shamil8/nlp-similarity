# Константы для модели и нашей выборки
PV_WORD_SIMILARITY = 0.5        # Коэффицент схожости слов данной задачи с моделью (принимает значения от 0 до 1).
MIN_COUNT_WORDS = 3       # Минимальное кол-во совпадающих слов в NLP и слов в данной задачи (если в задаче меньше слов чем здесь, то данная переменная уменьшается на 1)
SAMPLE_COUNT = 1000       # Кол-во выборки для прогноза

RATING_OWNER = 20       # если владелец данной задачи совпадает с владельцами задач из нашей выборки
RATING_WORD_SIMILARITY = 1      # если совпадает просто слово из название задачи с выборкой

