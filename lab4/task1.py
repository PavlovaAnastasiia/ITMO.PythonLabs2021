#Работа с оператором ветвления

from random import randint
import time

#ввод имен играющих
player1 = input("Введите имя первого игрока ")
player2 = input('Введите имя второго игрока ')

#Моделирование бросания кубика игроками
print(player1, 'бросает кубик!')
time.sleep(3)
n1 = randint(1,6)
print('Выпало число ', n1)

print(player2, 'бросает кубик!')
time.sleep(3)
n2 = randint(1,6)
print('Выпало число ', n2)

#Определение победителя
if n1 > n2:
    print(player1, 'победил(а)!')
elif n1 < n2:
    print(player2, 'победил(а)!')
else:
    print('Выпали одинаковые числа, победителя нет.')

