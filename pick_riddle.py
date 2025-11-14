import random
import json
import os, sys

def resource_path(relative_path):
    # PyInstaller sets sys._MEIPASS to the temp folder when running EXE
    if hasattr(sys, "_MEIPASS"):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Function to load data from a JSON file
def load_data(filename):
    # Load riddles and jokes from a JSON file, "r" for read, encoding in utf-8.
    path = resource_path(filename)
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

# Load riddle database using load_data function
data = load_data("assets/riddles.json")

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

# Function that picks random riddle from given category: returns riddle, determiner, and answer
def pick_random_riddle(category=None):
    # Gets "riddles" data from riddles.json
    riddles = data.get("riddles", {})

    # Check if riddles exist
    if not riddles:
        print("No riddles found.")
        return
    
    # Check if category is provided
    if category:
        # Check if the provided category exists in riddles.json
        if category not in riddles:
            print(f"Category '{category}' not found.")
            return
    else:
        # No category provided
        # Pick a random category from the available keys in riddles.json
        category = random.choice(list(riddles.keys()))

    # Picks out riddles from specific category 
    category_riddles = riddles[category]
    # Chooses random riddle from decided category
    riddle = random.choice(category_riddles)

    # Gets determiner from riddle
    determiner = riddle.get("determiner", "")
    # Gets answer from riddle: If "answer" exists answer is "answer", if not it is Unknown
    answer = riddle.get("answer", "Unknown")

    # Returns 'riddle' part of the variable called riddle, determiner, and answer
    return riddle['riddle'], determiner, answer