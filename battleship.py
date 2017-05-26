from boards import Board
from players import Player





class Game():
    print("\033c", end="")
    player_1 = ''
    player_2 = ''

    def __init__(self):
        self.setup()
        counter = 1
        while True:
            if self.even_odd(counter) == 1:
                self.game_turn(self.player_1, self.player_2)
                counter += 1
            else:
                self.game_turn(self.player_2, self.player_1)
                counter += 1

    def setup(self):
        self.player_1 = Player()
        self.player_1.board.clear_screen()
        self.player_1.board.ship_placement()
        self.player_1.board.clear_screen()
        input("Captain {}, your turn is complete. Please switch players and press any key ".format(self.player_1.name))
        self.player_1.board.clear_screen()
        self.player_2 = Player()
        self.player_2.board.clear_screen()
        self.player_2.board.ship_placement()
        self.player_2.board.clear_screen()
        input("Captain {}, your turn is complete. Please switch players and press any key ".format(self.player_2.name))

    def game_turn(self, player_shooter, player_shootee):
        player_shooter.board.clear_screen()
        player_shootee.board.print_board()
        player_shooter.board.fire(player_shooter, player_shootee)
        player_shooter.board.victory_check(player_shooter, player_shootee)

    def even_odd(self, count):
        if count % 2 != 0:
            return 1
        else:
            return 2


Game()
