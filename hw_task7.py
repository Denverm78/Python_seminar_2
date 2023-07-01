""" Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
Функцию hex используйте для проверки своего результата. """

def convert(number, basa):    
    result = ''
    while number > 0:
        result = h[(number % basa)] + result
        number //= basa
    return(result)

HEX_BASA = 16
h = '0123456789abcdef'
user_num = int(input("Введите целое число: "))
print("Введенное число:", user_num)

print(f"Число {user_num} в шестнадцатеричной системе равно {convert(user_num, HEX_BASA)}")
print("Строка для проверки:", hex(user_num))
