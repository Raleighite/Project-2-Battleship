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

    def take_cordinates(self, ship):
        location = input('''Where shall I order the {} to captain? Keep in mind she's {} long.
                                    (Give a location like A7) '''
                            .format(ship.name, ship.size)).strip().lower()
        cordinates = self.encode_cordinates(location)
        return cordinates

    def position_ships(self):
        '''Method populates board with players choosen positions'''
        for ship in self.ship_info:
            cordinates = self.take_cordinates(ship)
            if self.valid_cordinates_check(cordinates):
                orientation = input(
                                    '''Shall I position her horizontally
                                    captain? Y|N?: '''
                                    ).strip().lower()
                if orientation == "n":
                    counter = 0
                    cordinates_to_store = []
                    for row in range(cordinates[1],
                                     cordinates[1] + ship.size):
                        if self.check_ship_clearence((cordinates[0],
                                                 cordinates[1] + counter)):
                            cordinates_to_store.append((
                                                        cordinates[0],
                                                        cordinates[1] + counter
                                                        ))
                            counter += 1
                            continue
                        else:
                            print('''
                                  There's another ship in that position
                                   captain! I can't order the {} there!
                                    ''').format(ship.name)
                            self.position_ships()
                    ship.horizontal = False
                    ship.cordinates.append(cordinates_to_store)
                else:
                    counter = 0
                    cordinates_to_store = []
                    for column in range(cordinates[0], cordinates[0] + ship.size):
                        if self.check_ship_clearence((cordinates[0] + counter, cordinates[1])):
                            cordinates_to_store.append((cordinates[0] + counter, cordinates[1]))
                            counter += 1
                        else:
                            print('''There's another ship in that position
                                  captain! I can't order the {} there!''').format(
                                  ship.name)
                    ship.horizontal = True
                    ship.cordinates.append(cordinates_to_store)
            else:
                print("Captain, those cordinates...I don't understand them. Try again? ")
                self.take_cordinates()
    def encode_cordinates(self, cordinates):
        '''Converts user inputted cordinates into numeric form'''
        column = int(self.COLUMNS.index(cordinates[0]))
        row = int(cordinates[1:])
        return (column, row)

    def decode_cordinates(self,cordinates):
        column = self.COLUMNS[cordinates[0]]
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
        decoded_cordinates = self.decode_cordinates(cordinates)
        decoded_column = decoded_cordinates[0]
        decoded_row = decoded_cordinates[1]
        valid_columns = 'abcdefghij'
        if decoded_column in valid_columns:
            if 0 < decoded_row < 11:
                return True


Board()  # For Testing
