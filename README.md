# mathtool

Консольное приложение: решение уравнений и обработка числовых последовательностей.
Запускать из каталога репозитория.

```
py mathtool.py                         общая справка
py mathtool.py <команда> --help        справка по команде

py mathtool.py solve -a 1 -b -3 -c 2   решение уравнения (без -a -b -c — ввод с клавиатуры)
py mathtool.py stats --input numbers.txt   показатели последовательности (без --input — стандартный ввод)
py mathtool.py series --func sqplus --terms 6      сумма ряда по количеству слагаемых
py mathtool.py series --func sqplus --eps 0.0001   сумма ряда по точности
py mathtool.py integrate --func ratio --from 0 --to 20 --steps 1000   интеграл (левые прямоугольники)
```

Структура: `mathtool.py` — точка входа и ввод-вывод, `cli.py` — разбор параметров (argparse),
`calc/` — расчётная часть (`equation`, `stats`, `series`, `integration`), `tests.txt` — набор тестов.
Коды возврата: 0 — успех, 1 — ошибка в данных, 2 — ошибка в командной строке (argparse).