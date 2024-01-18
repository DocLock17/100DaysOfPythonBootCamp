#!/bin/python3
"""
Treasure Island Game.
"""

import sys

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

fork_1 = input("You're at a crossroad. Where do you want to go? \
Type \"left\" or \"right\"\n").lower()

if fork_1 != "left":
    print("You fell into a hole. Game Over.")
    sys.exit()

fork_2 = input("You've come to a lake. There is an island in the middle \
of the lake. Type \"wait\" to wait for a boat. \
Type \"swim\" to swim across.\n").lower()

if fork_2 != "wait":
    print("You get attacked by an angry trout. Game Over.")
    sys.exit()

fork_3 = input("You arrive at the island unharmed. There is a house with \
3 doors. One red, one yellow and one blue. \
Which colour do you choose?\n").lower()

if fork_3 == 'red':
    print("It's a room full of fire. Game Over.")
elif fork_3 == 'blue':
    print("You enter a room full of furocious beasts and get eaten. \
Game Over.")
elif fork_3 == 'yellow':
    print("You found the treasure! You Win!")
else:
    print("You chose a door that doesn't exists. Game Over.")
