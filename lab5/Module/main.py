from lab5.Module.CountResults import defineWin, countResult
from lab5.Module.NameAndRoll import namePlayer

def main():
    player1, player2 = namePlayer()
    player1Win, player2Win = defineWin(player1, player2)
    countResult(player1, player2, player1Win, player2Win)

main()