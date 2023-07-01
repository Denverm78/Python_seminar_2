import decimal
import math

while True:
    diametr = int(input("Введите диаметр окружности (не более 1000): "))
    if 0 < diametr < 1001: break
    else: 
        print("Вы ввели неверное значение, попробуйте еще раз")

decimal.getcontext().prec = 60
s = round((decimal.Decimal(math.pi) * diametr ** 2 / 4), 42)
l = round((2 * decimal.Decimal(math.pi) * diametr / 2), 42)
print("Площадь круга равна", s)
print("Длина окружности равна", l)