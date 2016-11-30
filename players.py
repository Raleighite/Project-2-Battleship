class Player:

    def __init__(self, name):
        self.name = input("What's your name captain? ")
        self.board = Board()
        self.attempted_shots = []

