import pandas as pd
from nlp_py.similarity import get_similarity

df = pd.read_csv('/app/data/tasks-from-mover.csv')
titles = df['name'].str.lower()

def get_similarity_tasks(text, user_id = '2be0ccf2-3608-11ea-9dc1-0242c0a85009'):
    nlp_words = get_similarity(text, True)
    tasks = []
    tmp = []

    # try to find
    for idx, words in enumerate(titles):
        for word in str(words).split():
            if word in nlp_words:
                if idx in tmp:
                    for index, [task_idx] in enumerate(tasks):
                        if task_idx == idx:
                            tasks[index][1] += 1  # [index][1] - it's a rating!
                else:
                    tmp.append(idx)
                    tasks.append([idx, 1])


    return user_id
