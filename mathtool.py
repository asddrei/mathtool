import math
import sys

MAX_VALUE = 10000
HELP_TEXT = """mathtool — решение уравнений вида A*x^2 + B*x + C = 0"""

def fmt(value):
    text = f"{value:.3f}"
    return "0.000" if text == "-0.000" else text


# БЛОК 1

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