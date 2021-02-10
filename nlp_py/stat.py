def pv_normalize_tasks(tasks, total):
    return [[times, rating / total] for rating, times, _ in tasks]


def math_expectation_x(data):
    mx = 0

    for x, p in data:
        mx += x * p

    return mx


def variance_x(data, mx=0):
    dx = 0

    if not mx:
        mx = math_expectation_x(data)

    for x, p in data:
        dx += (x - mx) ** 2 * p

    return dx

# Если дисперсия велика, то это указывает на существование
# значений случайной величины, которые сильно отклоняются от её
# математического ожидания, причем не все они маловероятны.
