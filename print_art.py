import json

# Opens ascii art json using utf-8 encoding, loads it into ascii_art_db
with open("ascii_art.json", encoding="utf-8") as f:
    ascii_art_db = json.load(f)

# Function to get art from art database
def get_art(name):
    art_entry = ascii_art_db.get(name)
    # If art is found return art
    if art_entry:
        return "\n".join(art_entry["art"])
    # If art is not found display error message
    return "Art not found."