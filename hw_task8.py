""" Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions. """
import fractions
import math

def sum_fract(as1, bs1, as2, bs2):
    chislit = as1 * bs2 + bs1 * as2
    znamenat = bs1 * bs2
    oz = math.gcd (chislit, znamenat)
    chislit = int(chislit / oz)
    znamenat = int(znamenat / oz)
    bs = znamenat   
    print("Сумма дробей равна", chislit, "/", znamenat)
    print("Строка для проверки")
    f1 = fractions.Fraction(as1, bs1)
    f2 = fractions. Fraction(as2, bs2)
    print(f1 + f2)
    print()
    
def mult_fract(am1, bm1, am2, bm2):
    am = am1 * am2
    bm = bm1 * bm2
    oz = math.gcd (am, bm)
    am = int(am / oz)
    bm = int(bm / oz)
    print("Произведение дробей равно", am, "/", bm)
    print("Строка для проверки")
    f1 = fractions.Fraction(am1, bm1)
    f2 = fractions. Fraction(am2, bm2)
    print(f1 * f2)
    print()

a_fract_1 = int(input("Введите числитель первой дроби a1: "))
b_fract_1 = int(input("Введите знаменатель первой дроби b1: "))
a_fract_2 = int(input("Введите числитель второй дроби a2: "))
b_fract_2 = int(input("Введите знаменатель второй дроби b2: "))
sum_fract(a_fract_1, b_fract_1, a_fract_2, b_fract_2)
mult_fract(a_fract_1, b_fract_1, a_fract_2, b_fract_2)


