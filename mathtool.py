"""Точка входа mathtool (этап 1: разбор параметров пока прежний, расчёт в calc.equation)."""
import sys

from calc import equation

HELP_TEXT = """mathtool — решение уравнений вида A*x^2 + B*x + C = 0

Использование:
    python mathtool.py                         вывод справки
    python mathtool.py --help                  вывод справки
    python mathtool.py solve                   ввод коэффициентов с клавиатуры
    python mathtool.py solve -a 1 -b -3 -c 2   решение с заданными коэффициентами

Коэффициенты A, B, C — целые числа, по модулю не превышающие 10000."""


def fmt(value):
    """Число с тремя знаками после запятой; без «-0.000»."""
    text = f"{value:.3f}"
    return "0.000" if text == "-0.000" else text


# ---------- 1. Разбор параметров командной строки (как в первой работе) ----------
args = sys.argv[1:]

if len(args) == 0 or args[0] == "--help":
    print(HELP_TEXT)
    sys.exit(0)

if args[0] != "solve":
    print(f"ОШИБКА: неизвестная команда «{args[0]}»", file=sys.stderr)
    sys.exit(1)

raw_a = raw_b = raw_c = None
if len(args) == 1:
    pass
elif len(args) == 7:
    if args[1] != "-a" or args[3] != "-b" or args[5] != "-c":
        print("ОШИБКА: неизвестный параметр (ожидается: -a, -b, -c)", file=sys.stderr)
        sys.exit(1)
    raw_a, raw_b, raw_c = args[2], args[4], args[6]
else:
    print("ОШИБКА: неверный набор параметров", file=sys.stderr)
    sys.exit(1)

# ---------- 2. Получение и преобразование данных ----------
try:
    if raw_a is None:
        a = int(input("Введите A: "))
        b = int(input("Введите B: "))
        c = int(input("Введите C: "))
    else:
        a, b, c = int(raw_a), int(raw_b), int(raw_c)
except ValueError:
    print("ОШИБКА: коэффициент не является целым числом", file=sys.stderr)
    sys.exit(1)

# ---------- 3. Проверка данных и расчёт (теперь в модуле calc.equation) ----------
try:
    equation.check_coefficients(a, b, c)
except ValueError as error:
    print(f"ОШИБКА: {error}", file=sys.stderr)
    sys.exit(1)

kind, d, roots = equation.solve(a, b, c)

# ---------- 4. Вывод результата ----------
print(f"Уравнение {kind}")
if d is not None:
    print(f"D = {d}")
if len(roots) == 2:
    print(f"x1 = {fmt(roots[0])}")
    print(f"x2 = {fmt(roots[1])}")
elif len(roots) == 1:
    print(f"x = {fmt(roots[0])}")
else:
    print("Действительных корней нет")

sys.exit(0)