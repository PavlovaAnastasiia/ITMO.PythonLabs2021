#Использование циклов
from random import randint
import time

player1 = input("Введите имя первого игрока ")
player2 = input('Введите имя второго игрока ')

player1Win = 0
player2Win = 0

for i in range(5):
    print(player1, 'бросает кубик!')
    time.sleep(1)
    n1 = randint(1,6)
    print('Выпало число ', n1)

    print(player2, 'бросает кубик!')
    time.sleep(1)
    n2 = randint(1,6)
    print('Выпало число ', n2)

    #определение результата
    if n1 > n2:
        player1Win += 1
    elif n1 < n2:
        player2Win +=1
    else:
        print('\tНичья!')

print('Игрок 1 победил ', player1Win, ' раз(а).')
print('Игрок 2 победил ', player2Win, ' раз(а).')
if player1Win > player2Win:
    print('В итоге победителем стал(а) ', player1)
elif player1Win < player2Win:
    print('В итоге победителем стал(а) ', player2)
elif player1Win == player2Win:
    print('\tПобедителя нет! Получился равный счет.')
