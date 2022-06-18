from random import randint
while True:
    x = randint(1,10)
    while True:
        r = float(input("Введите число "))
        if x != r:
            if x > r:
                print ("Загаданное число больше написанного")
            elif x < r:
                print("Загаданное число меньше написанного")
        elif x == r:
            print("Вы угадали число")
            break
