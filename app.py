# Import your Game class
from phrasehunter.game import Game


# Create your Dunder Main statement.
if __name__ == '__main__':
    new_game = Game(5)
    new_game.start_game()
    

# Inside Dunder Main:
## Create an instance of your Game class
## Start your game by calling the instance method that starts the game loop
