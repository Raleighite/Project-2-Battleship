from ships import Ship


class Board:

    VERTICAL_SHIP = '|'
    HORIZONTAL_SHIP = '-'
    EMPTY = 'O'
    MISS = '.'
    HIT = '*'
    SUNK = '#'
    COLUMNS = 'abcdefghijklmnopqrstuvwxyz'

    def __init__(self):
        self.board_size = 10
        self.board = []
        self.ship_info = [
            Ship("Aircraft Carrier", 5),
            Ship("Battleship", 4),
            Ship("Submarine", 3),
            Ship("Cruiser", 3),
            Ship("Patrol Boat", 2)
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
            location = input('''Where shall I order the {} to captain? Keep in mind she's {} long.
                                    (Give a location like A7) '''
                                 ).format(ship.name, ship.size).strip().lower()
            cordinates = encode_cordinates(location)
            if valid_cordinates_check(location):
                orientation = input("Shall I position her horizontally captain? Y|N?: "
                                    ).strip().lower()
                if orientation == "n":
                    counter = 0
                    for row in range(cordinates[1], cordinates[1]+ship.size):
                        if check_ship_clearence((cordinates[0], cordinates[1]+counter)):
                            counter += 1
                            continue
                        else:
                            print("There's another ship in that position captain! I can't order the {} there!").format(ship.name)
                            break
                    ship.horizontal = False
                else:
                    counter = 0
                    for column in range()
                    ship.horizontal = False
                ship.coordinates.append(encode_cordinates(location))

    def encode_cordinates(self, cordinates):
        '''Converts user inputted cordinates into numeric form'''
        column = COLUMNS.index(cordinates[0])
        row = cordinates[1:]
        return (column, row)

    def check_ship_clearence(self, cordinates):
        '''Checks to see if ships desired location conflicts with an
        existing ship's location'''
        for ship in self.ship_info:
            if cordinates in ship.cordinates:
                return False
            else:
                return True

    def valid_cordinates_check(self, cordinates):
        '''Checks the provided location entered by user is valid'''
        valid_columns = 'abcdefghij'
        if cordinates[0] in valid_columns:
            if 0 < cordinates[1:] < 11:
                return True


Board()  # For Testing
