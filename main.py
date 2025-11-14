from pdb import main
import print_art
import pick_riddle
import levels

riddle_db = pick_riddle.load_data("riddles.json")


def main():
    current_level = "beginning"

    while current_level is not None:
        #print(print_art.get_art("pocket_watch"))
            current_level = levels.level_function(current_level)

    print("The End.")

if __name__ == "__main__":
    main()
