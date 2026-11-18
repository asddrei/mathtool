"""Суммы знакочередующихся рядов (расчётная часть, без ввода-вывода)."""
import math

MAX_TERMS = 10000       # наибольшее значение --terms
MAX_EPS = 0.0001        # наибольшее значение --eps (самая грубая точность)
DIGITS = math.ceil(-math.log10(MAX_EPS))  # знаков после запятой при выводе (4)


def sign(n):
    """Знак слагаемого: нечётные плюс, чётные минус."""
    if n % 2 == 0:
        return -1
    return 1


def term_sqplus(n):
    """n-е слагаемое ряда 1/(1^2+1) - 1/(2^2+1) + ..."""
    return sign(n) / (n * n + 1)


def term_third(n):
    """n-е слагаемое ряда 1/3 - 1/6 + 1/9 - ..."""
    return sign(n) / (3 * n)


# Таблица рядов: имя -> (функция слагаемого, запись формулы)
FORMULAS = {
    "sqplus": (term_sqplus, "S = 1/(1^2+1) - 1/(2^2+1) + 1/(3^2+1) - ..."),
    "third":  (term_third,  "S = 1/3 - 1/6 + 1/9 - 1/12 + ..."),
}


def check_terms(terms):
    """Проверяет количество слагаемых; иначе ValueError."""
    if not 1 <= terms <= MAX_TERMS:
        raise ValueError(f"количество слагаемых вне диапазона 1..{MAX_TERMS}")


def sum_by_terms(term, count):
    """Сумма первых count слагаемых; term -- функция слагаемого."""
    result = 0
    for n in range(1, count + 1):
        result += term(n)
    return result