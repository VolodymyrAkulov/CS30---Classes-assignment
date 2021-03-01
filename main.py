# Course: CS 30
# Period: 1
# Date created: 28/02/2021
# Date last modified: 28/02/2021
# Name: Volodymyr Akulov
# Description: Classes Assignment

# Imports
from GlobalVar import p
from map import Map

# Map
map = Map()

# Loop so the interaction is continous
while True:
    # Border
    print("\n" + 18 * "-" + "Map" + 18 * "-")

    # Printing the map
    map.print()

    # Border
    print(40 * "-")

    # Taking input and making it lowercase
    x = input("North\nSouth\nWest\nEast\nKill\n\nExit\n\n")
    x = x.lower()

    # Moving the charachter and other logic
    if x == "north" and p.pos > 4:
        p.pos = p.pos - 5
        print(f"\nYou moved {x}")
    elif x == "south" and p.pos < 20:
        p.pos = p.pos + 5
        print(f"\nYou moved {x}")
    elif x == "west" and p.pos != 0 and p.pos != 5 and\
            p.pos != 10 and p.pos != 15 and p.pos != 20:
        p.pos = p.pos - 1
        print(f"\nYou moved {x}")
    elif x == "east" and p.pos != 4 and p.pos != 9 and\
            p.pos != 14 and p.pos != 19 and p.pos != 24:
        p.pos = p.pos + 1
        print(f"\nYou moved {x}")
    elif x == "exit":
        break
    elif x == 'kill' and p.pos == 24:
        print('!!!YOU WIN!!!')
        break
    elif x == 'kill':
        p.EnemyPos.remove(p.pos)
    else:
        print("Thats not a direction you can move in try again")
