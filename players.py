from boards import Board

class Player:

    def __init__(self):
        self.name = input("What's your name captain? ")
        self.board = Board()
        self.attempted_shots = []

