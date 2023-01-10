import pygame

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