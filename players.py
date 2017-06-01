from boards import Board

class Player:

    def __init__(self):
        self.name = input("What's your name captain? ")
        self.board = Board()
        self.attempted_shots = []

    # def hide_board(self):
    #     for row in self.board.board:
    #         for spot in row:
    #             spot == 'O'
