# Importing termcolor library
from termcolor import colored

# Creating tile class


class Tile:
    name = "Nothing"
    info = "a blank space"
    info2 = "No advantage"
    Token = " "

# Creating 4 categories of tiles


class Mud(Tile):
    name = "Mud"
    info = "Muddy ground is difficult to traverse."
    info2 = "Optimal terrain for picking enemies off at a distance."
    Token = colored('M', 'blue')


class Dirt(Tile):
    name = "Dirt"
    info = "Very standard fighting ground."
    info2 = "Grants no advantage."
    Token = colored('D', 'white')


class Grass(Tile):
    name = "Grass"
    info = "Grassy land very easy to manouver in."
    info2 = "Recommended for hand to hand combat."
    Token = colored('G', 'green')


class Stone(Tile):
    name = "Stone"
    info = "Hard floor. difficult to stand and manouver on this rough surface"
    info2 = "Conducts magic very easily."
    Token = colored('S', 'red')

# List to chose between tile types
TokenTiles = [Mud, Dirt, Grass, Stone]
