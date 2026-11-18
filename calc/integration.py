"""Численное интегрирование методом левых прямоугольников (без ввода-вывода)."""
import math

MAX_STEPS = 100000  # наибольшее число прямоугольников


def f_ratio(x):
    """F(x) = x / (x + 1)."""
    return x / (x + 1)


def f_root(x):
    """F(x) = sqrt(x^2 + 1)."""
    return math.sqrt(x * x + 1)


# Таблица функций: имя -> (функция, формула, нижняя граница, верхняя граница,
# строгие ли границы: True -- сами границы недопустимы, промежуток открытый)
FUNCTIONS = {
    "ratio": (f_ratio, "F(x) = x / (x + 1)",   0, 20, False),
    "root":  (f_root,  "F(x) = sqrt(x^2 + 1)", -5, 5, True),
}


def check_params(name, start, end, steps):
    """Проверяет пределы и число шагов до расчёта; иначе ValueError."""
    _, _, low, high, strict = FUNCTIONS[name]
    if not (math.isfinite(start) and math.isfinite(end)):
        raise ValueError("пределы интегрирования должны быть конечными числами")
    if start >= end:
        raise ValueError("начальный предел не меньше конечного")
    for limit in (start, end):
        if strict:
            outside = limit <= low or limit >= high
        else:
            outside = limit < low or limit > high
        if outside:
            raise ValueError(f"предел {limit} вне промежутка функции {name}")
    if not 1 <= steps <= MAX_STEPS:
        raise ValueError(f"количество шагов вне диапазона 1..{MAX_STEPS}")


def integrate(func, start, end, steps):
    """Интеграл методом левых прямоугольников; func -- подынтегральная функция."""
    dx = (end - start) / steps
    result = 0
    for i in range(steps):
        x = start + i * dx  # заново, а не накоплением x += dx
        result += func(x) * dx
    return result