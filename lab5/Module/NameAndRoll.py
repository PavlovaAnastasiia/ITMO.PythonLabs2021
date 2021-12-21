import time
from random import randint

def namePlayer():
    player1 = input("Введите имя первого игрока ")
    player2 = input('Введите имя второго игрока ')
    return player1, player2

def rollDice(player):
    print(player, 'бросает кубик!')
    time.sleep(1)
    points = randint(1, 6)
    print('Выпало число ', points)
    return points