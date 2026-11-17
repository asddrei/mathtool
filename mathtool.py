"""Точка входа mathtool: выбор команды, ввод-вывод, коды возврата."""
import sys

import cli
from calc import equation


def fmt(value):
    """Число с тремя знаками после запятой; без «-0.000»."""
    text = f"{value:.3f}"
    return "0.000" if text == "-0.000" else text


def read_coefficient(name):
    """Запрашивает с клавиатуры целый коэффициент."""
    try:
        return int(input(f"Введите {name}: "))
    except ValueError:
        raise ValueError("коэффициент не является целым числом") from None


def handle_solve(args):
    """Команда solve: возвращает код завершения."""
    given = [args.a is not None, args.b is not None, args.c is not None]
    if any(given) and not all(given):
        raise ValueError("укажите все три коэффициента либо ни одного")
    if not any(given):  # режим ввода с клавиатуры
        args.a = read_coefficient("A")
        args.b = read_coefficient("B")
        args.c = read_coefficient("C")

    equation.check_coefficients({"A": args.a, "B": args.b, "C": args.c})
    kind, d, roots = equation.solve(args.a, args.b, args.c)

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
    return 0


HANDLERS = {
    "solve": handle_solve,
}


def main(argv):
    """Разбирает параметры, вызывает обработчик, возвращает код завершения."""
    parser = cli.build_parser()
    args = parser.parse_args(argv)
    if args.command is None:
        parser.print_help()
        return 0
    if args.command not in HANDLERS:  # команды появятся на следующих этапах
        print(f"ОШИБКА: команда {args.command} пока не реализована", file=sys.stderr)
        return 1
    try:
        return HANDLERS[args.command](args)
    except OSError as error:
        print(f"ОШИБКА: файл не открывается: {error.filename}", file=sys.stderr)
        return 1
    except ValueError as error:
        print(f"ОШИБКА: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))