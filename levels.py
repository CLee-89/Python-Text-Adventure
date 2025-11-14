import json
import os
import platform
import pick_riddle

os_name = platform.system()

keys = None
player = "You: "
enemy = "Sphinx: "

riddles = []
riddle_intros = []
riddle_answers = []
riddles_solved = 0
riddles_asked = 0
response_map = {0: 1, 2: 2, 5: 3}
end_game_intro_played = False

if os_name == "Windows":
    import msvcrt

    def wait_key():
        print("Press any key...\n")
        msvcrt.getch()
        os.system('cls')

    def clear_screen():
        os.system('cls')

elif os_name == "Linux" or os_name == "Darwin":
    import curses

    def wait_key():
        def inner(scr):
            scr.addstr("Press any key...\n")
            scr.refresh()
            scr.getch()

        curses.wrapper(inner)
        os.system('clear')

    def clear_screen():
        os.system('clear')

else:
    raise Exception("Unsupported OS")

def load_data(filename):
    # Load riddles and jokes from a JSON file, "r" for read, encoding in utf-8.
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
    
data = load_data("level_dialogue.json")
# Load riddle database using load_data function from pick_riddle.py
riddle_db = pick_riddle.load_data("riddles.json")

def riddle_check(riddle_answer, player_answer):
    # Format player answer to have no spaces and be lowercase
    player_answer = player_answer.replace(" ", "").lower()

    if "|" in riddle_answer:
        # Split riddle_answer into multiple valid answers
        valid_answers = riddle_answer.split("|")
        # Check if player answer matches any of the valid answers
        return player_answer in [ans.replace(" ", "").lower() for ans in valid_answers]
    # Check if player answer matches riddle answer
    return player_answer == riddle_answer

def level_function(level):

    global riddles_asked, riddles_solved, end_game_intro_played

    match level:
        case "beginning":
            clear_screen()
            dialogue = data[level][0].get("dialogue", "")
            print(dialogue, '\n')
            wait_key()
            return data[level][0].get("next_level", "")
        case "end game":
            end_game_data = data[level][0]
            num_dialogues = len(end_game_data)

            clear_screen()

            if not end_game_intro_played:
                for i in range(num_dialogues):
                    if (i + 1) > 3:
                        print("Sphinx:", end_game_data[f"dialogue{i+1}"], '\n')
                    else: 
                        print(end_game_data[f"dialogue{i+1}"], '\n')
                    wait_key()
                print("You: Ok?")
                wait_key()
                
                end_game_intro_played = True


            if riddles_asked in response_map:
                response_number = response_map[riddles_asked]
                print("Sphinx:", riddle_db["responses"][0].get(f"inter{response_number}", ""), '\n')
                wait_key()
                print("You:", riddle_db["responses"][0].get(f"player_response{response_number}", ""), '\n')
                wait_key()
                joke_riddle, joke_answer = pick_riddle.pick_random_joke(riddle_db)
                print("Sphinx:", joke_riddle, '\n')
                wait_key()
                print("Sphinx:", joke_answer, '\n')
                wait_key()
                print("Sphinx:", riddle_db["responses"][0].get(f"enemy_response{response_number}", ""), '\n')
                wait_key()
                

            for i in range(len(riddles)):
                determiner, riddle_string = riddles[i]
                riddle_answer = riddle_answers[i]
                clear_screen()
                print_art.get_art()
                print("Sphinx:", riddle_intros[riddles_asked], '\n')
                wait_key()
                print(f"Sphinx: {riddle_string}\n")
                riddles_asked += 1

                guess = input(f"{determiner}").strip()

                if riddle_check(riddle_answer, guess):
                    riddles_solved += 1

                print ("correct answers: ", riddles_solved, " out of ", riddles_asked)
                wait_key()

            return "end_game"
        case _:
            # Grabs data from data, returns "" if key is not found
            dialogue = data[level][0].get("dialogue", "")
            action1 = data[level][0].get("action1", "")
            action2 = data[level][0].get("action2", "")
            event1 = data[level][0].get("event1", "")
            event2 = data[level][0].get("event2", "")
            action_choice = 0
            first_attempt = True

            # Input validation loop
            while True:
                clear_screen()
                print(dialogue, '\n')
                print(action1)
                print(action2)

                if first_attempt:
                    action_choice = input("\nChoose an action (1 or 2)... ").strip() # strip removes extra spaces
                    first_attempt = False
                else:
                    action_choice = input("\nInvalid choice. Please choose an action (1 or 2)... ").strip()
                if action_choice in ("1", "2"):
                    break

            clear_screen()

             # Print corresponding event based on user choice
            print(f'{event1 if action_choice == "1" else event2}\n')
            eventid = data[level][0].get("eventid1", "") if action_choice == "1" else data[level][0].get("eventid2", "")
            wait_key()

            # Get riddle parts from pick_riddle.py
            riddle_string, riddle_determiner, riddle_answer = pick_riddle.pick_random_riddle(eventid)

            # Adds space after determiner if it exists
            if riddle_determiner:
                riddle_determiner = riddle_determiner + " "
            
            # Format riddle answer to have no spaces and be lowercase
            riddle_answer = riddle_answer.replace(" ", "").lower()
            riddle_answers.append(riddle_answer)

            # Append riddle parts to riddles list
            riddles.append((riddle_determiner, riddle_string))
            riddle_intros.append(riddle_db["responses"][0].get(eventid, ""))

            return data[level][0].get("next_level", "")