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