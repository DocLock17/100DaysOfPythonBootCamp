#!/bin/python3
"""
Guess the number game.
"""

import random

TITLE = """
 ::::::::  :::    ::: :::::::::: ::::::::   ::::::::  ::: 
:+:    :+: :+:    :+: :+:       :+:    :+: :+:    :+: :+: 
+:+        +:+    +:+ +:+       +:+        +:+        +:+ 
:#:        +#+    +:+ +#++:++#  +#++:++#++ +#++:++#++ +#+ 
+#+   +#+# +#+    +#+ +#+              +#+        +#+ +#+ 
#+#    #+# #+#    #+# #+#       #+#    #+# #+#    #+#     
 ########   ########  ########## ########   ########  ### 
"""

def play_a_round(limit, answer):
    """
    One round
    """
    while limit>0:
        print("\nYou have "+str(limit)+" guesses remaining,")
        guess = int(input("Guess a guess guesser?: "))
        if guess > answer:
            limit -= 1
            print("Your guess was too high of a guess . . . try again")
        elif guess < answer:
            limit -= 1
            print("Your guess was too low of a guess . . . try again")
        else:
            limit -= 1
            print("\n\nYou guessed a correct guess! Great Job Guesser!\n\n")
            break

while True:
    print(TITLE)
    print("\nWelcome to Guess! The number Guessing Game\n")
    next_game = input("\nWould you like to start a new game?(y/n): ")
    if next_game != 'y':
        break
    else:
        difficulty = input("\nChoose a guessing difficulty. Type easy(e) or hard(h): ")
        if difficulty.lower == 'hard' or difficulty.lower == 'h':
            GUESS_LIMIT = 5
        else:
            GUESS_LIMIT =10
        the_answer = random.randint(0, 101)
        # print(the_answer)
        play_a_round(GUESS_LIMIT, the_answer)
        