from boards import Board
from players import Player





class Game():
    player_1 = ''
    player_2 = ''

    def __init__(self):
        self.setup()
        counter = 1
        while True:
            if self.even_odd(counter) == 1:
                self.game_turn(player_1, player_2)
                counter += 1
            else:
                self.game_turn(player_2, player_1)
                counter += 1

    def setup(self):
        player_1 = Player()
        player_1.board.clear_screen()
        player_1.board.position_ships()
        player_1.board.clear_screen()
        input("Captain {}, your turn is complete. Please switch players and press any key ").format(player_1.name)
        player_1.board.clear_screen()
        player_2 = Player()
        player_2.board.clear_screen()
        player_2.board.position_ships()
        player_2.board.clear_screen()
        input("Captain {}, your turn is complete. Please switch players and press any key ").format(player_2.name)

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



	# Prompt user to hit enter to end their turn
	# Clear screen
	# Ask player 2 to enter their name
	# Create instance of Player() and set to name provided
	# Create instance of Board() and assign ownership to player 2
	# Ask player to place a ship for each ship they have (5 in total)
		# Check to make sure the provided location by user is valid
			# If not valid, inform user, and ask for location again
		# Ask player if they want ship to be horizontal
		# Check to see if ship overlaps any other ship
			# If conflict, inform user, and ask for another location
			# If no conflict, store ship location
				# Register ship location up from inital point if vertical, and to the right if horizontal
				# Remember to register all affected locations of ship based on umber of spaces it occupies
	# Prompt user to hit enter to end their turn
	# Clear screen
	# Inform player 1 it's their turn. Prompt them to hit enter to proceede
	# Clear screen
	# Game loop
		# Draw current player's board on left with ships and other player's misses and hits
		# Draw other player's board on left, with current players misses and hits
		# Ask current player where to fire
			# Check if location is valid
				# If not inform current player, and allow them to guess again
			# If valid, check to see if current player has guessed that location before
				# If so, inform current player ana allow them to guess again
			# Check to see if shot hits other player's ship
				# If so inform current player and mark a hit on the other player's board at the location
					# Subtract one from size of other player's ship
					# Check to see if the ship was sunk
						# If sunk, inform current player what ship was sank
							# Check to see if other player has any ships left
								# If not, inform current player
									# Announce current player is the winner
								# If other player has ships remaining do nothing and move on
						# If not, continue on
					# Allow current player to fire again ?
				# If miss, inform current player, and mark a miss on other player's map
				# Either way, store the guess in current player's guessed moves





Game()
