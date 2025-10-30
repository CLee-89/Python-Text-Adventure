import print_art
import print_riddle

data = print_riddle.load_data("riddles.json")

while True:
    print(print_art.get_art("pocket_watch"))

    # Example usage
    print_riddle.print_random_joke(data)
    print_riddle.print_random_riddle(data)

    break