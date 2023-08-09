def concatenate(a, b):
    """
    Вычисляется результат сложения двух строк
    :param a: первая строка
    :param b: вторая строка
    :return: результат конкатенации
    """
    if isinstance(a, str) and isinstance(b, str):
        return a + b
    return "Необходимо ввести строковые типы данных"


