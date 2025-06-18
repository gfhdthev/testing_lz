import math as m


def ygoreck(a, b, c, d, f):
    try:
        result = round((a+b)/(c-d)+m.sqrt(f), 4)
    except ZeroDivisionError:
        result = 'Деление на ноль невозможно'
    except ValueError:
        result = 'Невозможно извлечь конень из отрицательного числа'
    except TypeError:
        result = 'Введенные вами значения не являются числом'
    return result