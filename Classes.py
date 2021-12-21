class Player:

    def __init__(self):
        self.status = 0


class Round:
    
    def __init__(self):
        self.round = 0
        # player 1 joue
        # on vérifie si il y a un gagnant ou si le nombre de tour <=5
        # player 2 joue
        # on vérifie si il y a un gagnant ou si nbre tour <=4


# Board controlle le nombre et la disponibilité des cases de case
class Board:

    def __init__(self):
        self.board = [
            [0,0,0],
            [0,0,0],
            [0,0,0],
        ]
        print(len(self.board))