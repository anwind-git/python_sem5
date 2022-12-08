# Создайте программу для игры с конфетами человек против человека, бот против человека.

from random import randint

def InputData():
    play = int(input("С кем будем играть? (человек = 1 бот = 2): "))

    while play < 1 or play > 2:
        play = int(input("Выберете праильно игру! (человек = 1 бот = 2): "))

    lot = randint(1, 2)
    player1 = input("Имя первого игрока: ")
    if play == 1:
        player2 = input("Имя второго игрока: ")
    else:
        player2 = "бот Вася"

    candies = int(input("Cколько на столе лежит конфет: "))
    while candies < 29:
        candies = int(input("Введите больше 28: "))
        
    def Game():
        nonlocal candies
        nonlocal lot        
        if play == 1:
            sum_player1 = 0
            sum_player2 = 0
            while candies > 28:
                if lot == 1:
                    print(f"На столе осталось {candies} конфет")
                    number = int(input(
                        f"{player1} заберите со стола от 1-ой до 28 конфет. Сейчас у Вас в копилке {sum_player1} конфет: "))
                    print()
                    while number < 1 or number > 28:
                        number = int(
                            input(f"{player1} Введите число от 1 до 28: "))
                        print()
                    sum_player1 += number
                    candies -= number
                    lot = 2
                    if candies <= 28:
                        sum_player1 += sum_player2
                        sum_player2 -= sum_player2
                        break
                    print()
                if lot == 2:
                    print(f"На столе осталось {candies} конфет")
                    number = int(input(
                        f"{player2} заберите со стола от 1-ой до 28 конфет. Сейчас у Вас в копилке {sum_player2} конфет: "))
                    print()
                    while number < 1 or number > 28:
                        number = int(
                            input(f"{player2} Введите число от 1 до 28: "))
                        print()                    
                    sum_player2 += number
                    candies -= number
                    lot = 1
                    if candies <= 28:
                        sum_player2 += sum_player1
                        sum_player1 -= sum_player1
                        break                    
                    print()

            if sum_player1 > sum_player2:
                print(f"У {player1} победил")
            else:
                print(f"У {player2} победил")
        if play == 2:
            sum_player1 = 0
            sum_player2 = 0
            while candies > 28:
                if lot == 1:
                    print(f"На столе осталось {candies} конфет")
                    number = int(input(
                        f"{player1} заберите со стола от 1-ой до 28 конфет. Сейчас у Вас в копилке {sum_player1} конфет: "))
                    print()
                    while number < 1 or number > 28:
                        number = int(
                            input(f"{player1} Введите число от 1 до 28: "))
                        print()
                    sum_player1 += number
                    candies -= number
                    lot = 2
                    if candies <= 28:
                        sum_player1 += sum_player2
                        sum_player2 -= sum_player2
                        break
                    print()
                if lot == 2:
                    print(f"На столе осталось {candies} конфет")
                    number = randint(1, 28)
                    print(
                        f"{player2} забрал {number} конфет и у него теперь их {sum_player2}")
                    print()
                    sum_player2 += number
                    candies -= number
                    lot = 1
                    if candies <= 28:
                        sum_player2 += sum_player1
                        sum_player1 -= sum_player1
                        break                    
                    print()
                    
            print(f"{player1}: {sum_player1} конфет")
            print(f"{player2}: {sum_player2} конфет")
            if sum_player1 > sum_player2:
                print(f"{player1} победил")
            else:
                print(f"{player2} победил")
            
    Game()
    
InputData()