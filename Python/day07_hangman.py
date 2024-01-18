#!/bin/python3
""" 
This a complete implementation of a simple hangman game
build on stream to meet/exceed the requirements of the
100 days of coding python boot camp course from udemy.
"""

import random


TITLE = """
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \\ / _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                    __/ |                      
                   |___/
"""


gallows_list = ["""
  _______
 |/      |
 |
 |      
 |      
 |    
 |
_|___
""","""
  _______
 |/      |
 |      (_)
 |      
 |      
 |    
 |
_|___
""","""
  _______
 |/      |
 |      (_)
 |       |
 |      
 |    
 |
_|___
""","""
  _______
 |/      |
 |      (_)
 |      \\|
 |      
 |    
 |
_|___
""","""
  _______
 |/      |
 |      (_)
 |      \\|/
 |      
 | 
 |
_|___
""","""
  _______
 |/      |
 |      (_)
 |      \\|/
 |       |
 | 
 |
_|___
""","""
  _______
 |/      |
 |      (_)
 |      \\|/
 |       |
 |      /
 |
_|___
""","""
  _______
 |/      |
 |      (_)
 |      \\|/
 |       |
 |      / \\
 |
_|___
"""]


word_list = ['test']

def get_word_display(guessed_list, word):
    """
    Formats and displays the game board.
    """
    game_board_word = ""
    for each in word:
        if each in guessed_list:
            game_board_word += ' '+each+' '
        else:
            game_board_word += ' _ '
    return game_board_word

def get_wrong_guess_count(guessed_list, word):
    """
    Calculates wrong guesses.
    """
    # print(guessed_list)
    # print(word)
    wrong_guesses = 0
    for each in guessed_list:
        if each not in word:
            wrong_guesses += 1
            # print(wrong_guesses)
    return wrong_guesses

def run_game(word):
    """
    Runs game.
    """
    # print(word)
    # guessed_list = ['e']
    guessed_list = []
    solution_list = []
    while True:
        wrong_count = get_wrong_guess_count(guessed_list, word)
        print(gallows_list[wrong_count])
        print("\n")
        word_disp = get_word_display(guessed_list, word)
        print(word_disp)
        print("\n")
        if wrong_count > 6:
            print("ψ(｀∇´)ψ")
            print("\n")
            print("Sorry You Lose!")
            print("\n")
            break
        if ' _ ' not in word_disp:
            print("ଘ(੭ºัᴗºั)━☆ﾟ.*･")
            print("\n")
            print("You won!!")
            print("\n")
            break
        guess = input("Guess a letter: ")
        if guess.lower() == 'solve':
            player_solution = input("\nSolution?: ")
            if player_solution.lower() == word:
                print("\n")
                print("ଘ(੭ºัᴗºั)━☆ﾟ.*･")
                print("\n")
                print("You won!!")
                print("\n")
                break
            if player_solution.lower() in solution_list:
                print("\nYou have already tried this solution.\nIt is incorrect.")
            else:
                solution_list.append(player_solution)
                print("\nSorry that solution is incorrect!")
                guessed_list.append("%")
        elif len(guess) > 1 or len(guess) < 1:
            print("\nBad input please try again!\n")
        elif guess in guessed_list:
            print("\nYou already guessed the letter "+guess+"\nPlease Try Again!")
        else:
            guessed_list.append(guess)
        # print(guessed_list)

print(TITLE)
while True:
    game_flag = input("Would you like to start a new game? (y,n): ") #y Y yes YES
    if game_flag.lower() == 'y':
        run_game(random.choice(word_list))
    else:
        break
