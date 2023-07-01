""" Напишите программу банкомат.
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
операцией, даже ошибочной
✔ Любое действие выводит сумму денег """

def start_menu():
    action_user = int(input("Выберите действие: 1 - пополнить, 2 - снять, 0 - выйти: "))
    if action_user == 1:
        print("Выбрана опeрация пополнения.")
        add()    
    elif action_user == 2:
        print("Выбрана операция снятия.")
        remove()
    elif action_user == 0:
        print_sum()
        print("Пока-пока, всегда Вам рады, приходите еще!")
        exit()
    else:
        print("Не попали в нужную кнопку. Давайте попробуем еще раз.")
        start_menu()

def add():
    global sum_user
    global count_action
    if sum_user > LIMIT_RICH:
        sum_user = sum_user - sum_user * NALOG_RICH
    print("Вы можете пополнить сумму кратно 50")
    while True:
        add_user = float(input("Сколько вы хотите ввести? (кратно 50): "))
        if (add_user % 50 == 0): break
        else: print("Сумма должна быть кратна 50...")
    if (count_action % 3 != 0 or count_action == 0):
        sum_user = sum_user + add_user
    else:
        sum_user = sum_user + (add_user - int(add_user*COMISS_2))
    count_action += 1
    print_sum()
    start_menu()

def remove():
    global sum_user
    global count_action
    if sum_user > LIMIT_RICH:
        sum_user = sum_user - sum_user * NALOG_RICH
    remove_user = float(input("Сколько вы хотите снять?: "))
    comiss = remove_user * COMISS_1
    if comiss < MIN_COMISS:
        comiss = MIN_COMISS
    if comiss > MAX_COMISS:
        comiss = MAX_COMISS
    if count_action % 3 == 0:      
        comiss = comiss * COMISS_2   
    if ((remove_user + comiss) > sum_user):
        print("Недостаточно средств")
        start_menu()
    else:
        print("Заберите деньги")
        sum_user = sum_user - (remove_user + comiss)
        count_action += 1
        print_sum()
        start_menu()

def print_sum():
    print("На вашем счету ", round(sum_user, 2), " у.е.")            

MIN_COMISS = 30
MAX_COMISS = 600
COMISS_1 = 0.015
COMISS_2 = 0.03
NALOG_RICH = 0.1
LIMIT_RICH = 5_000_000
sum_user = 0
count_action = 0
count_sum = 0
start_menu()
