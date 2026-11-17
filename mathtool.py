"""Точка входа mathtool (этап 2: разбор параметров через argparse)."""
import sys

import cli
from calc import equation


def fmt(value):
    """Число с тремя знаками после запятой; без «-0.000»."""
    text = f"{value:.3f}"
    return "0.000" if text == "-0.000" else text


# ---------- 1. Разбор параметров (argparse) ----------
parser = cli.build_parser()
args = parser.parse_args(sys.argv[1:])

if args.command is None:  # команда не указана: справка и код 0
    parser.print_help()
    sys.exit(0)

if args.command != "solve":  # остальные команды появятся на следующих этапах
    print(f"ОШИБКА: команда {args.command} пока не реализована", file=sys.stderr)
    sys.exit(1)

# ---------- 2. Получение и преобразование данных ----------
given = [args.a is not None, args.b is not None, args.c is not None]
if any(given) and not all(given):
    print("ОШИБКА: укажите все три коэффициента либо ни одного", file=sys.stderr)
    sys.exit(1)

try:
    if not any(given):  # ввод с клавиатуры
        a = int(input("Введите A: "))
        b = int(input("Введите B: "))
        c = int(input("Введите C: "))
    else:
        a, b, c = args.a, args.b, args.c
except ValueError:
    print("ОШИБКА: коэффициент не является целым числом", file=sys.stderr)
    sys.exit(1)

# ---------- 3. Проверка данных и расчёт ----------
try:
    equation.check_coefficients(a, b, c)
except ValueError as error:
    print(f"ОШИБКА: {error}", file=sys.stderr)
    sys.exit(1)

kind, d, roots = equation.solve(a, b, c)

# ---------- 4. Вывод результата ----------
print(f"Уравнение {kind}")
if d is not None:
    print(f"Дискриминант: {d}")
if len(roots) == 2:
    print(f"x1 = {fmt(roots[0])}")
    print(f"x2 = {fmt(roots[1])}")
elif len(roots) == 1:
    print(f"x = {fmt(roots[0])}")
else:
    print("Действительных корней нет")

sys.exit(0)