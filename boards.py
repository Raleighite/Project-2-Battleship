import sys

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

    def clear_screen(self):
        print("\033c", end="")

    def print_board_heading(self):
        print("   " + " ".join([chr(c) for c in range(ord('A'),
                                ord('A') + self.board_size)
                                ]))
    def hide_board(self):
        self.board = []
        for rows in range(self.board_size):
            row = []
            for spot in range(self.board_size):
                row.append(self.EMPTY)
            self.board.append(row)

    def print_board(self):
        self.print_board_heading()
        row_num = 1
        for row in self.board:
            print(str(row_num).rjust(2) + " " + (" ".join(row)))
            row_num += 1

    def take_coordinates_placement(self, ship):
        self.clear_screen()
        self.print_board()
        location = input('''Where shall I order the {} to captain? Keep in mind she's {} long.
                                    (Give a location like A7) '''
                            .format(ship.name, ship.size)).strip().lower()
        return location

    def ship_placement(self):
        for ship in self.ship_info:
            self.location_input(ship)
            self.mark_locations(ship)
            self.clear_screen()

    def horizontal_input(self, ship):
        question = input("Shall I position her horizontally captain? Y/n?: ").strip().lower()
        if question == 'n':
            ship.horizontal = False
        else:
            ship.horizontal = True

    def location_input(self, ship):
        coordinates = self.take_coordinates_placement(ship)
        if self.valid_coordinates_check(coordinates):
            coordinates = self.encode_coordinates(coordinates)
            self.horizontal_input(ship)
            counter = 0
            for i in range(ship.size):
                row = None
                column = None
                if ship.horizontal:
                    row = coordinates[0]
                    column = coordinates[1] + counter
                else:
                    row = coordinates[0] + counter
                    column = coordinates[1]
                if self.check_ship_clearance((row, column)):
                    pass
                else:
                    input("There's a ship already there. Press a key to try again! ")
                    self.reset_ship(ship)
                if self.wont_grow_too_much((row, column)):
                    ship.coordinates.append((row, column))
                    counter += 1
                else:
                    self.clear_screen()
                    input("Ship won't fit there captain! Press a key to try again! ")
                    self.reset_ship(ship)
        else:
            self.clear_screen()
            input("Those are not valid coordinates! Press a key to try again! ")
            self.reset_ship(ship)

    def reset_ship(self, ship):
        ship.horizontal = None
        ship.coordinates = []
        self.location_input(ship)

    def mark_locations(self, ship):
        marker = ''
        if ship.horizontal:
            marker = self.HORIZONTAL_SHIP
        else:
            marker = self.VERTICAL_SHIP
        for coordinate in ship.coordinates:
            self.board[coordinate[0]][coordinate[1]] = marker


    def encode_coordinates(self, coordinates):
        '''Converts user inputted coordinates into numeric form'''
        column = int(self.COLUMNS.index(coordinates[0]))
        row = int(coordinates[1:]) - 1
        return row, column

    def decode_coordinates(self,coordinates):
        ''''Converts numeric form coordinates into human readable alphanumeric'''
        column = self.COLUMNS[coordinates[0]]
        row = coordinates[1] + 1
        return row, column

    def check_ship_clearance(self, coordinates):
        '''Checks to see if ships desired location conflicts with an
        existing ship's location. For some reason this loop is running multiple times.'''
        clear = None
        for ship in self.ship_info:
            try:
                if ship.coordinates == None or []:
                    continue
                elif coordinates in ship.coordinates:
                    clear = False
                    return clear
                else:
                    clear = True
            except IndexError:
                clear = True
        return clear

    def valid_coordinates_check(self, coordinates):
        '''Checks the provided location entered by user is valid'''
        try:
            decoded_column = coordinates[0]
            try:
                decoded_row = int(coordinates[1:])
            except ValueError:
                return False
            valid_columns = 'abcdefghij'
            if decoded_column in valid_columns:
                if decoded_row < 0 or decoded_row > 10:
                    return False
                else:
                    return True
        except IndexError:
            return False

    def wont_grow_too_much(self, coordinates):
        if coordinates[0] and coordinates[1] > 9:
            if coordinates[0] and coordinates[1] < 0:
                return False
        else:
            return True

    def fire(self, player_shooter, player_shootee):
        self.clear_screen()
        player_shootee.board.print_board()
        shot_coordinates = input("Where shall we fire Captain {}? Give coordinate like A7 > ".format(player_shooter.name))
        if self.valid_coordinates_check(shot_coordinates):
            shot_coordinates = self.encode_coordinates(shot_coordinates)
            if shot_coordinates in player_shooter.attempted_shots:
                input("You have already tried to shoot there. Press any key to try again ")
                self.fire(player_shooter, player_shootee)
            did_hit = None
            for ship in player_shootee.board.ship_info:
                if shot_coordinates in ship.coordinates:
                    self.clear_screen()
                    did_hit = True
                    input("You hit the {}".format(ship.name))
                    ship.damage()
                    if ship.sunk():
                        self.clear_screen()
                        input("WooHoo! You sank the {} Captain!".format(ship.name))
                        player_shootee.board.ship_info.remove(ship)
            player_shooter.attempted_shots.append(shot_coordinates)
            if did_hit:
                player_shootee.board.mark(shot_coordinates, True)
            else:
                player_shootee.board.mark(shot_coordinates, False)
        else:
            self.clear_screen()
            input("Those are not valid coordinates captain. Press any key to try again ")
            self.fire(player_shooter, player_shootee)

    def mark(self, coordinates, hit):
        row, column = coordinates
        if hit == True:
            self.board[row][column] = Board.HIT
        else:
            input("You missed!")
            self.board[row][column] = Board.MISS

    def victory_check(self, player_shooter, player_shootee):
        if len(player_shootee.board.ship_info) <= 0:
            self.clear_screen()
            print("Congrats {}! You Win!!!!!".format(player_shooter.name))
            print("*" * 20)
            input("Press any key to exit")
            sys.exit()

