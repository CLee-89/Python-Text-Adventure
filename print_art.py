import os, sys
import json

# Function to get resource path for files
def resource_path(relative_path):
    # PyInstaller sets sys._MEIPASS to the temp folder when running EXE
    if hasattr(sys, "_MEIPASS"):
        # Get the base path from PyInstaller's temp folder
        base_path = sys._MEIPASS
    else:
        # Get the absolute path to the current directory
        base_path = os.path.abspath(".")
    # Return the joined path
    return os.path.join(base_path, relative_path)

# Load ascii art database using resource_path function
json_file = resource_path("assets/ascii_art.json")
# Opens ascii art json using utf-8 encoding, loads it into ascii_art_db
with open(json_file, encoding="utf-8") as f:
    ascii_art_db = json.load(f)
    
# Function to get art from art database
def get_art(name):
    art_entry = ascii_art_db.get(name)
    # If art is found return art
    if art_entry:
        return "\n".join(art_entry["art"])
    # If art is not found display error message
    return "Art not found."