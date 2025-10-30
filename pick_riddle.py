import random
import json

def load_data(filename):
    # Load riddles and jokes from a JSON file, "r" for read, encoding in utf-8.
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

# Function that picks random joke and returns riddle and answer
def pick_random_joke(data):
    # Print a random joke from the JSON data.
    jokes = data.get("jokes", [])
    # If jokes is empty or not found show error message
    if not jokes:
        print("No jokes found.")
        return
    # Chooses one joke at random
    joke = random.choice(jokes)

    # Gets riddle from joke
    riddle = joke['riddle']
    #Gets answer from joke
    answer = joke.get("answer", "Unknown")

    return riddle, answer
    print(f"JOKE:\n{joke['riddle']}")
    print(f" {joke['answer']}\n")

# Function that picks random riddle from given category: returns riddle, determiner, and answer
def pick_random_riddle(data, category=None):
    # Gets "riddles" data from riddles.json
    riddles = data.get("riddles", {})

    # If riddles is emtpy display error message and return
    if not riddles:
        print("No riddles found.")
        return
    
    # If category is not None
    if category:
        # If category is missing display error message and return
        if category not in riddles:
            print(f"Category '{category}' not found.")
            return
    else:
        # Pick a random category
        category = random.choice(list(riddles.keys()))

    # Picks out riddles from specific category 
    category_riddles = riddles[category]
    # Chooses random riddle from decided category
    riddle = random.choice(category_riddles)

    # Gets determiner from riddle
    determiner = riddle.get("determiner", "")
    # Gets answer from riddle: If "answer" exists answer is "answer", if not it is Unknown
    answer = riddle.get("answer", "Unknown")

    return riddle['riddle'], determiner, answer

    print(f"RIDDLE ({category.upper()}):\n{riddle['riddle']}")
    print(f" {determiner} {answer}".strip() + "\n")