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
        self.ship_info = [
            ("Aircraft Carrier", 5),
            ("Battleship", 4),
            ("Submarine", 3),
            ("Cruiser", 3),
            ("Patrol Boat", 2)
        ]
        self.board_size = 10
        self.board = []
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
        # For each ship in 'ship_info' create an instance of Ship()
        # Ask player where they want to place the ship
            # Check if player provides a valid location
            # Check if location doesn't have a conflicting ship
            # If either of the above fails, inform player and retry input
        # Save the ships location


Board()  # For Testing
