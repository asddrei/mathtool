import math #пригодится мне для квадратного корня math.sqrt()
import sys # sys.argv (параметры), sys.exit() (код возврата), sys.stderr (поток ошибок, проверял на output.txt)

MAX_VALUE = 10000 #Значения всех коэффициентов целые, по модулю не превышающие 10 000
HELP_TEXT = """mathtool — решение уравнений вида A*x^2 + B*x + C = 0

Использование:
    python mathtool.py                         вывод справки
    python mathtool.py --help                  вывод справки
    python mathtool.py solve                   ввод коэффициентов с клавиатуры
    python mathtool.py solve -a 1 -b -3 -c 2   решение с заданными коэффициентами

Коэффициенты A, B, C — целые числа, по модулю не превышающие 10000.""" #Справка, которая выведется в случае --help
#Тройные ковычки нужны для многострочной строки

def fmt(value): #вспомогательная функция для красивого округления и форматирования чисел, тестил в test2.py
    text = f"{value:.3f}"
    return "0.000" if text == "-0.000" else text


# БЛОК 1

args = sys.argv[1:] #sys.argv — список строк, введённых при запуске

if len(args) == 0 or args[0] == "--help":
    print(HELP_TEXT)
    sys.exit(0) #выводим справку, если нету 

if args[0] != "solve": #если первый элемент не solve, то выдает ошибку (1)
    print(f"ОШИБКА: неизвестная команда «{args[0]}»", file=sys.stderr)
    sys.exit(1)

raw_a = raw_b = raw_c = None #значений из командной строки нету
if len(args) == 1: 
    pass #пропускаем, значение также остаются по нулям
elif len(args) == 7:
    if args[1] != "-a" or args[3] != "-b" or args[5] != "-c": #проверяем, что именно коэффициенты a, b, c, а не никакие не z w и т.д
        print("ОШИБКА: неизвестный параметр (ожидается: -a, -b, -c)", file=sys.stderr)
        sys.exit(1)
    raw_a, raw_b, raw_c = args[2], args[4], args[6] #если все ок, то присваиваем им значения (будут в виде строк)
else:
    print("ОШИБКА: неверный набор параметров", file=sys.stderr) #если не 1 и не 7 параметров
    sys.exit(1)



#Блок 2

#try/except - механизм обработки исключений (ошибок), который защищает программу от внезапного «вылета» и падения.
try: 
    if raw_a is None: #если ничего не задано, то просит пользователя самого ввести значения
        a = int(input("Введите A: "))
        b = int(input("Введите B: "))
        c = int(input("Введите C: "))
    else: #или же значения пришли из командной строки
        a, b, c = int(raw_a), int(raw_b), int(raw_c)
except ValueError: # int("abc"), int("5.5"), int("") ---> ValueError
    print("ОШИБКА: коэффициент не является целым числом", file=sys.stderr)
    sys.exit(1)



#Блок 3

#Данная ситуация не является исключительной и проверяется ветвлением if, а также используется abs() -- модуль числа
if abs(a) > MAX_VALUE or abs(b) > MAX_VALUE or abs(c) > MAX_VALUE:
    print("ОШИБКА: значение вне допустимого диапазона", file=sys.stderr)
    sys.exit(1)