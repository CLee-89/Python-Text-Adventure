import json

with open("ascii_art.json", encoding="utf-8") as f:
    ascii_art_db = json.load(f)

def get_art(name):
    art_entry = ascii_art_db.get(name)
    if art_entry:
        return "\n".join(art_entry["art"])
    return "Art not found."