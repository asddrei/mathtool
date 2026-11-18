"""Показатели числовой последовательности (расчётная часть, без ввода-вывода)."""
import math

MAX_COUNT = 20     # наибольшее количество чисел
MAX_ABS = 10000    # наибольшее значение числа по модулю


def check_values(values):
    """Проверяет список чисел; при недопустимых данных возбуждает ValueError."""
    if len(values) == 0:
        raise ValueError("последовательность пуста")
    if len(values) > MAX_COUNT:
        raise ValueError(f"чисел больше {MAX_COUNT}")
    for value in values:
        if not math.isfinite(value):
            raise ValueError(f"значение {value} не является конечным числом")
        if abs(value) > MAX_ABS:
            raise ValueError(f"значение {value} по модулю больше {MAX_ABS}")


def total(values):
    """Сумма чисел."""
    result = 0
    for value in values:
        result += value
    return result


def mean(values):
    """Среднее арифметическое."""
    return total(values) / len(values)


def sum_squares(values):
    """Сумма квадратов чисел."""
    result = 0
    for value in values:
        result += value ** 2
    return result


def rms(values):
    """Среднее квадратическое: корень из (сумма квадратов / N)."""
    return math.sqrt(sum_squares(values) / len(values))


def sum_squared_deviations(values):
    """Сумма квадратов отклонений от среднего (вспомогательная функция)."""
    center = mean(values)
    result = 0
    for value in values:
        result += (value - center) ** 2
    return result


def variance(values):
    """Дисперсия: сумма (Ai - среднее)^2 / N (в два прохода)."""
    return sum_squared_deviations(values) / len(values)


def sd_population(values):
    """СКО: корень из дисперсии (по N)."""
    return math.sqrt(variance(values))


def sd_sample(values):
    """Стандартное отклонение (по N - 1); для одного числа не существует (None)."""
    if len(values) < 2:
        return None
    return math.sqrt(sum_squared_deviations(values) / (len(values) - 1))


def minimum(values):
    """Наименьшее из чисел."""
    result = values[0]
    for value in values:
        if value < result:
            result = value
    return result


def maximum(values):
    """Наибольшее из чисел."""
    result = values[0]
    for value in values:
        if value > result:
            result = value
    return result


def count_positive(values):
    """Количество чисел больше нуля."""
    result = 0
    for value in values:
        if value > 0:
            result += 1
    return result


def count_negative(values):
    """Количество чисел меньше нуля."""
    result = 0
    for value in values:
        if value < 0:
            result += 1
    return result

# Таблица вывода: (подпись, функция, формат). Порядок строк = порядок вывода.
REPORT = [
    ("Количество",     len,            "d"),
    ("Сумма",          total,          ".3f"),
    ("Ср. арифм.",     mean,           ".3f"),
    ("Сумма кв.",      sum_squares,    ".3f"),
    ("Ср. кв.",        rms,            ".3f"),
    ("Дисперсия",      variance,       ".3f"),
    ("СКО",            sd_population,  ".3f"),
    ("Станд. откл.",   sd_sample,      ".3f"),
    ("Наименьшее",     minimum,        ".3f"),
    ("Наибольшее",     maximum,        ".3f"),
    ("Положительных",  count_positive, "d"),
    ("Отрицательных",  count_negative, "d"),
]