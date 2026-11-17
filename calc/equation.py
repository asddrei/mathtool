"""Решение уравнения A*x^2 + B*x + C = 0 (расчётная часть, без ввода-вывода)."""
import math

MAX_VALUE = 10000  # предельное по модулю значение коэффициентов


def check_coefficients(coefficients):
    """Проверяет коэффициенты; при недопустимых данных возбуждает ValueError.

    coefficients -- словарь вида {"A": 1, "B": -3, "C": 2}.
    """
    for name, value in coefficients.items():
        if abs(value) > MAX_VALUE:
            raise ValueError(f"коэффициент {name} вне допустимого диапазона")
    if coefficients["A"] == 0 and coefficients["B"] == 0:
        raise ValueError("это не уравнение, неизвестное отсутствует")


def solve(a, b, c):
    """Решает уравнение; ничего не печатает.

    Возвращает кортеж (вид уравнения, дискриминант, список корней).
    Для линейного уравнения дискриминант равен None.
    """
    if a == 0:
        return "линейное", None, [-c / b]
    d = b * b - 4 * a * c
    if d > 0:
        root = math.sqrt(d)
        return "квадратное", d, [(-b + root) / (2 * a), (-b - root) / (2 * a)]
    if d == 0:
        return "квадратное", d, [-b / (2 * a)]
    return "квадратное", d, []