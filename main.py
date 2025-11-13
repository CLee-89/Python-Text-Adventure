import print_art
import pick_riddle

riddle_db = pick_riddle.load_data("riddles.json")

while True:
    print(print_art.get_art("pocket_watch"))

    # Example usage
    pick_riddle.print_random_joke(riddle_db)
    pick_riddle.print_random_riddle(riddle_db)

    break