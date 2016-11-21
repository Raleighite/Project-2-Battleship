from boards import Board
from players import Player



def clear_screen():
    print("\033c", end="")

class Game():

    def __init__(self):
        player_1 = Player()
        Player_2 = Player()
# Game class
	# Ask player 1 to enter their name
	# Create instance of Player() and set to name provided
	# Create instance of Board() and assign ownership to player 1
	# Ask player to place a ship for each ship they have (5 in total)
		# Check to make sure the provided location by user is valid
		# Ask player if they want the ship to be horizontal
		# Check to see if ship overlaps any other ship
			# If conflict inform user and ask for a different location to place ship
			# If no conflict store ship location
				# Register ship location up from initial point if vertical or to the right if horizontal
				# Remember to register all affected locations of ship based on number of spaces it occupies
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






