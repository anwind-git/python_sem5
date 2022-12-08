# Создайте программу для игры в "Крестики-нолики"

pole = [1, 2, 3, 4, 5, 6, 7, 8, 9]
player = "НОЛИКИ!"
victory = 0
i = 0

while i < 10:
    print("-------------")
    print(f"| {pole[0]} | {pole[1]} | {pole[2]} |")
    print(f"| {pole[3]} | {pole[4]} | {pole[5]} |")
    print(f"| {pole[6]} | {pole[7]} | {pole[8]} |")
    print("-------------")
    if victory == 0 and i == 9:
        print("НИЧЬЯ :-|")
        break
    if victory == 1:
        if player == "НОЛИКИ!":
            print("КРЕСТИКИ ПОБЕДИЛИ!!!")
        else:
            print("НОЛИКИ ПОБЕДИЛИ!!!")
        break    
    if victory == 0:
        number = int(input(f"{player} Введите номер поля: "))
        if number > 0 and number < 10:
            if pole[number - 1] != "O" and pole[number - 1] != "X":
                if player == "НОЛИКИ!":
                    pole[number - 1] = 'O'
                    player = "КРЕСТИКИ!"
                else:
                    pole[number - 1] = 'X'
                    player = "НОЛИКИ!"
                i += 1
            else:
                print(f"{player} ПОЛЕ УЖЕ ИСПОЛЬЗОВАНО! Введите другой номер.")
        else:
            print(f"{player} ПОЛЕ НЕСУЩЕСТВУЕТ! Введите другой номер.")
            
        if number > 0 and number < 10:
            if (pole[0] == 'O' and pole[1] == 'O' and pole[2] == 'O') or (pole[0] == 'X' and pole[1] == 'X' and pole[2] == 'X'):
                victory = 1
            if (pole[3] == 'O' and pole[4] == 'O' and pole[5] == 'O') or (pole[3] == 'X' and pole[4] == 'X' and pole[5] == 'X'):
                victory = 1
            if (pole[6] == 'O' and pole[7] == 'O' and pole[8] == 'O') or (pole[6] == 'X' and pole[7] == 'X' and pole[8] == 'X'):
                victory = 1
            if (pole[0] == 'O' and pole[3] == 'O' and pole[6] == 'O') or (pole[0] == 'X' and pole[3] == 'X' and pole[6] == 'X'):
                victory = 1
            if (pole[1] == 'O' and pole[4] == 'O' and pole[7] == 'O') or (pole[1] == 'X' and pole[4] == 'X' and pole[7] == 'X'):
                victory = 1
            if (pole[2] == 'O' and pole[5] == 'O' and pole[8] == 'O') or (pole[2] == 'X' and pole[5] == 'X' and pole[8] == 'X'):
                victory = 1
            if (pole[0] == 'O' and pole[4] == 'O' and pole[8] == 'O') or (pole[0] == 'X' and pole[4] == 'X' and pole[8] == 'X'):
                victory = 1
            if (pole[2] == 'O' and pole[4] == 'O' and pole[6] == 'O') or (pole[2] == 'X' and pole[4] == 'X' and pole[6] == 'X'):
                victory = 1