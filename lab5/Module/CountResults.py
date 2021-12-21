from lab5.Module.NameAndRoll import rollDice

def defineWin(player1, player2):
    player1Win = 0
    player2Win = 0

    for i in range(5):
        n1 = rollDice(player1)
        n2 = rollDice(player2)
        if n1 > n2:
            player1Win += 1
        elif n1 < n2:
            player2Win +=1
        else:
            print('\tНичья!')
    return player1Win, player2Win

def countResult (player1, player2, player1Win, player2Win):
    print('Игрок 1 победил ', player1Win, ' раз(а).')
    print('Игрок 2 победил ', player2Win, ' раз(а).')
    if player1Win > player2Win:
        print('В итоге победителем стал(а) ', player1)
    elif player1Win < player2Win:
        print('В итоге победителем стал(а) ', player2)
    elif player1Win == player2Win:
        print('\tПобедителя нет! Получился равный счет.')