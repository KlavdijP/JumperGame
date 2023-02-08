import pygame
import os
import json

def load_image(src, sc1, sc2, flipped=False):
    if flipped:
        return pygame.transform.flip(pygame.transform.scale(pygame.image.load("./assets/" + src + ".png"), (sc1, sc2)), True, False)
    return pygame.transform.scale(pygame.image.load("./assets/" + src + ".png"), (sc1, sc2))

def read_file(src):
    try:
        # Open the file in read mode
        with open(src, 'r') as file:
            # Read the contents of the file
            file_contents = file.read()
            print(file_contents)
            return file_contents
    except FileNotFoundError:
        # Create a new file if the file doesn't exist
        with open(src, 'w') as file:
            file.write("0")
            print("file created")
            return "0"

def write_file(src, text):
    with open(src, "w+") as file:
        file.write(str(text))
        print("Writing in file: %s", text)


def return_json_data():
    filepath = "data.json"
    if os.path.exists(filepath):
        f = open(filepath)
        data = json.load(f)
        return data
    else:
        create_new_json()
        return_json_data()

def create_new_json():
    filepath = "data.json"
    dictionary = {
        "player_name": "SKYFRIK",
        "score": 0,
        "high_score": 0,
        "rigs" : 0,
        "microchips": 0,
    }
    with open(filepath, "w") as f:
        json.dump(dictionary, f)