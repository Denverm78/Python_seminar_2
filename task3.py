def convert(number, basa):    
    result = ''
    while number > 0:
        result = str(number % basa) + result
        number //= basa
    return(result)


BIN_BASA = 2
OCT_BASA = 8
user_num = int(input("Введите целое число: "))
print("Введенное число:", user_num)

print(f"Число {user_num} в двоичной системе равно {convert(user_num, BIN_BASA)}")
print("Строка для проверки:", bin(user_num))
print(f"Число {user_num} в восьмеричной системе равно {convert(user_num, OCT_BASA)}")
print("Строка для проверки:", oct(user_num))