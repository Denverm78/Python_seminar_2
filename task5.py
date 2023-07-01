import math

print("Решим квадратное уравнение типа ax^2 + bx + c = 0")
a = float(input("Введите а: "))
b = float(input("Введите b: "))
c = float(input("Введите c: "))

discrim = b ** 2 - 4 * a * c
 
if discrim > 0:
    x1 = (-b + math.sqrt(discrim)) / (2 * a)
    x2 = (-b - math.sqrt(discrim)) / (2 * a)
    print("x1=", x1)
    print("x2=", x2)
elif discrim == 0:
    x = -b / (2 * a)
    print("x =", x)
else:
    print("Уравнение корней не имеет")

# С комплексными, правда, не хочется разбираться, я даже не знаю, что это такое.
# Думаю, что и на семинаре все бы зависли с ними.
# Уверен, что они мне не пригодятся в текущей жизни =)