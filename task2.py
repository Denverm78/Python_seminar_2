import sys

data = [5, 2.68, 'Hello', (1, 2), 5==5, 5, 2.68, 'Hello', (1, 2), 5==5]
count = 1
for i in data:
    print(count, i, id(i), sys.getsizeof(i), hash(i), 'целое_число' if isinstance(i, int) else '',\
        'строка' if isinstance(i, str) else '', 'вещественное_число' if isinstance(i, float) else '',\
        'кортеж' if isinstance(i, tuple) else '')
    count += 1