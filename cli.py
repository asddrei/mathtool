"""Разбор параметров командной строки (argparse)."""
import argparse


def build_parser():
    """Создаёт и возвращает разборщик параметров."""
    parser = argparse.ArgumentParser(
        prog="mathtool",
        description="mathtool — расчёты над уравнениями и числовыми последовательностями",
        allow_abbrev=False,
    )
    commands = parser.add_subparsers(dest="command")

    # solve: коэффициенты не обязательны (без них — ввод с клавиатуры)
    solve = commands.add_parser(
        "solve", help="решение уравнения A*x^2 + B*x + C = 0", allow_abbrev=False)
    solve.add_argument("-a", type=int, help="коэффициент A (целое, по модулю не более 10000)")
    solve.add_argument("-b", type=int, help="коэффициент B")
    solve.add_argument("-c", type=int, help="коэффициент C")

    # stats: --input не обязателен (без него числа читаются из стандартного ввода)
    stats = commands.add_parser(
        "stats", help="показатели числовой последовательности", allow_abbrev=False)
    stats.add_argument("--input", help="файл с числами (без него — стандартный ввод)")

    # series: ровно один из --terms и --eps
    ser = commands.add_parser("series", help="сумма ряда", allow_abbrev=False)
    ser.add_argument("--func", required=True, help="какой ряд суммировать")
    stop = ser.add_mutually_exclusive_group(required=True)
    stop.add_argument("--terms", type=int, help="остановка по количеству слагаемых (1..10000)")
    stop.add_argument("--eps", type=float, help="остановка по точности (больше 0, не грубее 0.0001)")

    # integrate: все параметры обязательны
    integ = commands.add_parser(
        "integrate", help="численное интегрирование (левые прямоугольники)", allow_abbrev=False)
    integ.add_argument("--func", required=True, help="какую функцию интегрировать")
    integ.add_argument("--from", dest="start", type=float, required=True,
                       help="нижний предел интегрирования")
    integ.add_argument("--to", dest="end", type=float, required=True,
                       help="верхний предел интегрирования (больше нижнего)")
    integ.add_argument("--steps", type=int, required=True,
                       help="число прямоугольников (1..100000)")
    return parser