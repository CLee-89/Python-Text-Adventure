# Text Adventure Game - created by Christopher Lee
from pdb import main
import levels


def main():
    quit = False

    # Main game loop
    while quit == False:
        current_level = "beginning"

        # Level loop
        while current_level is not None:
                current_level = levels.level_function(current_level)

        # Asks if player wants to play again
        play_again = ""
        while play_again not in ["y", "n"]:
            print("Game Over. Do you wish to play again? (y/n)")
            play_again = input().strip().lower()

            if play_again == "y":
                break
            elif play_again == "n":
                quit = True
                
        # Resets global variables in levels.py
        levels.reset_globals()
        
# Calls main function to start game
if __name__ == "__main__":
    main()
