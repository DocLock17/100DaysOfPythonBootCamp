#!/bin/python3
"""
Rock Paper Scissors
"""

# import myMod
import random

# print(myMod.pi)

# random_float = random.random()
# print(random_float)

# Rock
ROCK_HAND = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
PAPER_HAND = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
SCISSORS_HAND = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


all_hands = [ROCK_HAND, PAPER_HAND, SCISSORS_HAND]

print("Rock, Paper, Scissors, SHOOT!")
PLAYER_SELECTION = input("What is your selection? (Try r, p, or s) :")
if PLAYER_SELECTION.lower() == "r":
    PLAYER_SELECTION = 0
elif PLAYER_SELECTION.lower() == "p":
    PLAYER_SELECTION = 1
elif PLAYER_SELECTION.lower() == "s":
    PLAYER_SELECTION = 2

bot_selection = random.randint(0, 2)
# bot_selection = all_hands[random_selection]
print("\n")
print("Your Selection:")
print(all_hands[PLAYER_SELECTION])
print("\n")
print("Computer Selection:")
print(all_hands[bot_selection])
print("\n")
if PLAYER_SELECTION == 0 and bot_selection == 0 or \
    PLAYER_SELECTION == 1 and bot_selection == 1 or \
        PLAYER_SELECTION == 2 and bot_selection== 2:
    print("Selections Draw, NO Winner this round")

elif PLAYER_SELECTION == 0 and bot_selection == 1 or \
    PLAYER_SELECTION == 1 and bot_selection == 2 or \
        PLAYER_SELECTION == 2 and bot_selection == 0:
    print("You Lose! Please Try Again!")

elif PLAYER_SELECTION == 0 and bot_selection == 2 or \
    PLAYER_SELECTION == 1 and bot_selection == 0 or \
        PLAYER_SELECTION == 2 and bot_selection == 1:
    print("You Win! Great Work!!!")

G = True

while not G:
    print("derp")

# def turn_right():
#     [turn_left() for x in range(3)]
# while not at_goal():
#     if front_is_clear() == True:
#         if right_is_clear():
#             turn_right()
#             move()
#         else:
#             move()
#     else:
#         if right_is_clear():
#             turn_right()
#             move()
#         else:
#             turn_left()        
# def turn_right():
#     [turn_left() for x in range(3)]
# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#             move()
#     else:
#         turn_left()
