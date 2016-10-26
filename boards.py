from ships import Ship


class Board:

    VERTICAL_SHIP = '|'
    HORIZONTAL_SHIP = '-'
    EMPTY = 'O'
    MISS = '.'
    HIT = '*'
    SUNK = '#'

    def __init__(self, hidden=False):
        self.hidden = hidden
        self.board_size = 10
        self.board = []
        self.ship_info = [
            Ship(("Aircraft Carrier", 5)),
            Ship(("Battleship", 4)),
            Ship(("Submarine", 3)),
            Ship(("Cruiser", 3)),
            Ship(("Patrol Boat", 2))
        ]
        for rows in range(self.board_size):
            row = []
            for spot in range(self.board_size):
                row.append(self.EMPTY)
            self.board.append(row)
        self.print_board()

    def print_board_heading(self):
        print("   " + " ".join([chr(c) for c in range(ord('A'),
                                ord('A') + self.board_size)
                                ]))

    def print_board(self):
        self.print_board_heading()
        row_num = 1
        for row in self.board:
            print(str(row_num).rjust(2) + " " + (" ".join(row)))
            row_num += 1

    def position_ships(self):
        '''Method populates board with players choosen positions'''
        for ship in self.ship_info:
            ship.location = input('''Where do you want to place your {}, it's {} spaces}?
                                 Enter a location like A7: '''
                                 ).format(ship.name, ship.size).strip().lower()
            orientation = input("Place the ship horizontally? Y|N?: "
                                ).strip().lower()
            if orientation == "y":
                ship.horizontal = True

    def check_ship_clearence(self, location):
        '''Checks to see if ships desired location conflicts with an
        existing ship's location'''

    def valid_location_input(self, location):
        '''Checks the provided location entered by user is valid'''


Board()  # For Testing
