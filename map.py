# Course: CS 30
# Period: 1
# Date created: 2/10/21
# Date last modified: 2/10/25
# Name: Volodymyr Akulov
# Description: Modules and maps

import random
import Dictionary
from GlobalVar import p
from termcolor import colored

# creates and prints out map

MapString = []
p.EnemyPos = []
p.pos = 0

for i in range(25):
    MapString.append(random.choice(Dictionary.TokenTiles))

for i in range(random.randint(5, 10)):
    p.EnemyPos.append(random.randint(0, 23))


class Map:
    def __init__(self):
        """Map with placeholders to replace"""
        self.formatted_map = (
            "╔═══════╦═══════╦═══════╦═══════╦═══════╗\n"
            "║       ║       ║       ║       ║       ║\n"
            "║ {} ║ {} ║ {} ║ {} ║ {} ║               \n"
            "║       ║       ║       ║       ║       ║\n"
            "╠═══════╬═══════╬═══════╬═══════╬═══════╣\n"
            "║       ║       ║       ║       ║       ║\n"
            "║ {} ║ {} ║ {} ║ {} ║ {} ║               \n"
            "║       ║       ║       ║       ║       ║\n"
            "╠═══════╬═══════╬═══════╬═══════╬═══════╣\n"
            "║       ║       ║       ║       ║       ║\n"
            "║ {} ║ {} ║ {} ║ {} ║ {} ║               \n"
            "║       ║       ║       ║       ║       ║\n"
            "╠═══════╬═══════╬═══════╬═══════╬═══════╣\n"
            "║       ║       ║       ║       ║       ║\n"
            "║ {} ║ {} ║ {} ║ {} ║ {} ║               \n"
            "║       ║       ║       ║       ║       ║\n"
            "╠═══════╬═══════╬═══════╬═══════╬═══════╣\n"
            "║       ║       ║       ║       ║       ║\n"
            "║ {} ║ {} ║ {} ║ {} ║ {} ║               \n"
            "║       ║       ║       ║       ║       ║\n"
            "╚═══════╩═══════╩═══════╩═══════╩═══════╝  "
        )
        self.tile = MapString[p.pos]

    def print(self):
        """Function to print the map"""
        def form(i, x):
            """Replacing placeholders"""
            if i in p.EnemyPos and i == p.pos:
                return f"֎[{x}]֎"
            elif i == 24 and i == p.pos:
                return f"✰[{x}]✰"
            elif i == p.pos:
                return f" [{x}] "
            elif i in p.EnemyPos:
                return f"֎ {x} ֎"
            elif i == 24:
                return f"✰ {x} ✰"
            else:
                return f"  {x}  "

        # Printing the actuall map with placeholders
        print(self.formatted_map.format(*(form(i, x.Token)
                                          for i, x in enumerate(MapString))))

        # Legend to help the player
        print(17 * "-" + "Legend" + 17 * "-")
        print(
            f"{colored('M','blue')} - Mud     \n"
            f"{colored('D','white')} - Dirt   \n"
            f"{colored('G','green')} - Grass  \n"
            f"{colored('S','red')} - Stone    \n"
            "֎ - Enemy                        \n"
            "✰ - Goal                          "

        )

        # making it look good
        print(40 * "-")
        tile = MapString[p.pos]
        self.tile = MapString[p.pos]

        # Information about the tile
        print(f"You are currently standing on {tile.name}")
        print(f"{tile.info}\n{tile.info2}")
        return tile
