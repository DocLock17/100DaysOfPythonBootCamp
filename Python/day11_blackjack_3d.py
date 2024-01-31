#!/bin/bash
"""
TODO: we will implement this game on stream.
"""
import random

TITLE = """
:::::::::  :::            :::      ::::::::  :::    ::: ::::::::::: :::      ::::::::  :::    ::: 
:+:    :+: :+:          :+: :+:   :+:    :+: :+:   :+:      :+:   :+: :+:   :+:    :+: :+:   :+:  
+:+    +:+ +:+         +:+   +:+  +:+        +:+  +:+       +:+  +:+   +:+  +:+        +:+  +:+   
+#++:++#+  +#+        +#++:++#++: +#+        +#++:++        +#+ +#++:++#++: +#+        +#++:++    
+#+    +#+ +#+        +#+     +#+ +#+        +#+  +#+       +#+ +#+     +#+ +#+        +#+  +#+   
#+#    #+# #+#        #+#     #+# #+#    #+# #+#   #+#  #+# #+# #+#     #+# #+#    #+# #+#   #+#  
#########  ########## ###     ###  ########  ###    ###  #####  ###     ###  ########  ###    ###"""

DECK_DICT = {
  1 : {
    "rank"  :1,
    "suit"  :"Diamond",
    "black_jack_score"  :11,
    "image" :r"""
.::::::::::::
|A         ||
|          ||
|    /\    ||
|   /  \   ||
|   \  /   ||
|    \/    ||
|          ||
|         A|'
 ``````````  
"""},
  2 : {
    "rank"  :2,
    "suit"  :"Diamond",
    "black_jack_score"  :2,
    "image" :r"""
.::::::::::::
|2         ||
|          ||
|    /\    ||
|   /  \   ||
|   \  /   ||
|    \/    ||
|          ||
|         2|'
 ``````````  
"""},
  3 : {
    "rank"  :3,
    "suit"  :"Diamond",
    "black_jack_score"  :3,
    "image" :r"""
.::::::::::::
|3         ||
|          ||
|    /\    ||
|   /  \   ||
|   \  /   ||
|    \/    ||
|          ||
|         3|'
 ``````````  
"""},
  4 : {
    "rank"  :4,
    "suit"  :"Diamond",
    "black_jack_score"  :4,
    "image" :r"""
.::::::::::::
|4         ||
|          ||
|    /\    ||
|   /  \   ||
|   \  /   ||
|    \/    ||
|          ||
|         4|'
 ``````````  
"""},
  5 : {
    "rank"  :5,
    "suit"  :"Diamond",
    "black_jack_score"  :5,
    "image" :r"""
.::::::::::::
|5         ||
|          ||
|    /\    ||
|   /  \   ||
|   \  /   ||
|    \/    ||
|          ||
|         5|'
 ``````````  
"""},
  6 : {
    "rank"  :6,
    "suit"  :"Diamond",
    "black_jack_score"  :6,
    "image" :r"""
.::::::::::::
|6         ||
|          ||
|    /\    ||
|   /  \   ||
|   \  /   ||
|    \/    ||
|          ||
|         6|'
 ``````````  
"""},
  7 : {
    "rank"  :7,
    "suit"  :"Diamond",
    "black_jack_score"  :7,
    "image" :r"""
.::::::::::::
|7         ||
|          ||
|    /\    ||
|   /  \   ||
|   \  /   ||
|    \/    ||
|          ||
|         7|'
 ``````````  
"""},
  8 : {
    "rank"  :8,
    "suit"  :"Diamond",
    "black_jack_score"  :8,
    "image" :r"""
.::::::::::::
|8         ||
|          ||
|    /\    ||
|   /  \   ||
|   \  /   ||
|    \/    ||
|          ||
|         8|'
 ``````````  
"""},
  9 : {
    "rank"  :9,
    "suit"  :"Diamond",
    "black_jack_score"  :9,
    "image" :r"""
.::::::::::::
|9         ||
|          ||
|    /\    ||
|   /  \   ||
|   \  /   ||
|    \/    ||
|          ||
|         9|'
 ``````````  
"""},
  10 : {
    "rank"  :10,
    "suit"  :"Diamond",
    "black_jack_score"  :10,
    "image" :r"""
.::::::::::::
|10        ||
|          ||
|    /\    ||
|   /  \   ||
|   \  /   ||
|    \/    ||
|          ||
|        10|'
 ``````````  
"""},
  11 : {
    "rank"  :11,
    "suit"  :"Diamond",
    "black_jack_score"  :10,
    "image" :r"""
.::::::::::::
|J         ||
|          ||
|    /\    ||
|   /  \   ||
|   \  /   ||
|    \/    ||
|          ||
|         J|'
 ``````````  
"""},
  12 : {
    "rank"  :12,
    "suit"  :"Diamond",
    "black_jack_score"  :10,
    "image" :r"""
.::::::::::::
|Q         ||
|          ||
|    /\    ||
|   /  \   ||
|   \  /   ||
|    \/    ||
|          ||
|         Q|'
 ``````````  
"""},
  13 : {
    "rank"  :13,
    "suit"  :"Diamonds",
    "black_jack_score"  :10,
    "image" :r"""
.::::::::::::
|K         ||
|          ||
|    /\    ||
|   /  \   ||
|   \  /   ||
|    \/    ||
|          ||
|         K|'
 ``````````  
"""},
  14 : {
    "rank"  :1,
    "suit"  :"Hearts",
    "black_jack_score"  :11,
    "image" :r"""
.::::::::::::
|A         ||
|   _  _   ||
|  ( \/ )  ||
|   \  /   ||
|    \/    ||
|          ||
|          ||
|         A|'
 ``````````  
"""},
  15 : {
    "rank"  :2,
    "suit"  :"Hearts",
    "black_jack_score"  :2,
    "image" :r"""
.::::::::::::
|2         ||
|   _  _   ||
|  ( \/ )  ||
|   \  /   ||
|    \/    ||
|          ||
|          ||
|         2|'
 ``````````  
"""},
  16 : {
    "rank"  :3,
    "suit"  :"Hearts",
    "black_jack_score"  :3,
    "image" :r"""
.::::::::::::
|3         ||
|   _  _   ||
|  ( \/ )  ||
|   \  /   ||
|    \/    ||
|          ||
|          ||
|         3|'
 ``````````  
"""},
  17 : {
    "rank"  :4,
    "suit"  :"Hearts",
    "black_jack_score"  :4,
    "image" :r"""
.::::::::::::
|4         ||
|   _  _   ||
|  ( \/ )  ||
|   \  /   ||
|    \/    ||
|          ||
|          ||
|         4|'
 ``````````  
"""},
  18 : {
    "rank"  :5,
    "suit"  :"Hearts",
    "black_jack_score"  :5,
    "image" :r"""
.::::::::::::
|5         ||
|   _  _   ||
|  ( \/ )  ||
|   \  /   ||
|    \/    ||
|          ||
|          ||
|         5|'
 ``````````  
"""},
  19 : {
    "rank"  :6,
    "suit"  :"Hearts",
    "black_jack_score"  :6,
    "image" :r"""
.::::::::::::
|6         ||
|   _  _   ||
|  ( \/ )  ||
|   \  /   ||
|    \/    ||
|          ||
|          ||
|         6|'
 ``````````  
"""},
  20 : {
    "rank"  :7,
    "suit"  :"Hearts",
    "black_jack_score"  :7,
    "image" :r"""
.::::::::::::
|7         ||
|   _  _   ||
|  ( \/ )  ||
|   \  /   ||
|    \/    ||
|          ||
|          ||
|         7|'
 ``````````  
"""},
  21 : {
    "rank"  :8,
    "suit"  :"Hearts",
    "black_jack_score"  :8,
    "image" :r"""
.::::::::::::
|8         ||
|   _  _   ||
|  ( \/ )  ||
|   \  /   ||
|    \/    ||
|          ||
|          ||
|         8|'
 ``````````  
"""},
  22 : {
    "rank"  :9,
    "suit"  :"Hearts",
    "black_jack_score"  :9,
    "image" :r"""
.::::::::::::
|9         ||
|   _  _   ||
|  ( \/ )  ||
|   \  /   ||
|    \/    ||
|          ||
|          ||
|         9|'
 ``````````  
"""},
  23 : {
    "rank"  :10,
    "suit"  :"Hearts",
    "black_jack_score"  :10,
    "image" :r"""
.::::::::::::
|10        ||
|   _  _   ||
|  ( \/ )  ||
|   \  /   ||
|    \/    ||
|          ||
|          ||
|        10|'
 ``````````  
"""},
  24 : {
    "rank"  :11,
    "suit"  :"Hearts",
    "black_jack_score"  :10,
    "image" :r"""
.::::::::::::
|J         ||
|   _  _   ||
|  ( \/ )  ||
|   \  /   ||
|    \/    ||
|          ||
|          ||
|         J|'
 ``````````  
"""},
  25 : {
    "rank"  :12,
    "suit"  :"Hearts",
    "black_jack_score"  :10,
    "image" :r"""
.::::::::::::
|Q         ||
|   _  _   ||
|  ( \/ )  ||
|   \  /   ||
|    \/    ||
|          ||
|          ||
|         Q|'
 ``````````  
"""},
  26 : {
    "rank"  :13,
    "suit"  :"Hearts",
    "black_jack_score"  :10,
    "image" :r"""
.::::::::::::
|K         ||
|   _  _   ||
|  ( \/ )  ||
|   \  /   ||
|    \/    ||
|          ||
|          ||
|         K|'
 ``````````  
"""},
  27 : {
    "rank"  :1,
    "suit"  :"Clubs",
    "black_jack_score"  :11,
    "image" :r"""
.::::::::::::
|A         ||
|          ||
|    __    ||
|   (  )   ||
|  ( \/ )  ||
|    /\    ||
|          ||
|         A|'
 ``````````  
"""},
  28 : {
    "rank"  :2,
    "suit"  :"Clubs",
    "black_jack_score"  :2,
    "image" :r"""
.::::::::::::
|2         ||
|          ||
|    __    ||
|   (  )   ||
|  ( \/ )  ||
|    /\    ||
|          ||
|         2|'
 ``````````  
"""},
  29 : {
    "rank"  :3,
    "suit"  :"Clubs",
    "black_jack_score"  :3,
    "image" :r"""
.::::::::::::
|3         ||
|          ||
|    __    ||
|   (  )   ||
|  ( \/ )  ||
|    /\    ||
|          ||
|         3|'
 ``````````  
"""},
  30 : {
    "rank"  :4,
    "suit"  :"Clubs",
    "black_jack_score"  :4,
    "image" :r"""
.::::::::::::
|4         ||
|          ||
|    __    ||
|   (  )   ||
|  ( \/ )  ||
|    /\    ||
|          ||
|         4|'
 ``````````  
"""},
  31 : {
    "rank"  :5,
    "suit"  :"Clubs",
    "black_jack_score"  :5,
    "image" :r"""
.::::::::::::
|5         ||
|          ||
|    __    ||
|   (  )   ||
|  ( \/ )  ||
|    /\    ||
|          ||
|         5|'
 ``````````  
"""},
  32 : {
    "rank"  :6,
    "suit"  :"Clubs",
    "black_jack_score"  :6,
    "image" :r"""
.::::::::::::
|6         ||
|          ||
|    __    ||
|   (  )   ||
|  ( \/ )  ||
|    /\    ||
|          ||
|         6|'
 ``````````  
"""},
  33 : {
    "rank"  :7,
    "suit"  :"Clubs",
    "black_jack_score"  :7,
    "image" :r"""
.::::::::::::
|7         ||
|          ||
|    __    ||
|   (  )   ||
|  ( \/ )  ||
|    /\    ||
|          ||
|         7|'
 ``````````  
"""},
  34 : {
    "rank"  :8,
    "suit"  :"Clubs",
    "black_jack_score"  :8,
    "image" :r"""
.::::::::::::
|8         ||
|          ||
|    __    ||
|   (  )   ||
|  ( \/ )  ||
|    /\    ||
|          ||
|         8|'
 ``````````  
"""},
  35 : {
    "rank"  :9,
    "suit"  :"Clubs",
    "black_jack_score"  :9,
    "image" :r"""
.::::::::::::
|9         ||
|          ||
|    __    ||
|   (  )   ||
|  ( \/ )  ||
|    /\    ||
|          ||
|         9|'
 ``````````  
"""},
  36 : {
    "rank"  :10,
    "suit"  :"Clubs",
    "black_jack_score"  :10,
    "image" :r"""
.::::::::::::
|10        ||
|          ||
|    __    ||
|   (  )   ||
|  ( \/ )  ||
|    /\    ||
|          ||
|        10|'
 ``````````  
"""},
  37 : {
    "rank"  :11,
    "suit"  :"Clubs",
    "black_jack_score"  :10,
    "image" :r"""
.::::::::::::
|J         ||
|          ||
|    __    ||
|   (  )   ||
|  ( \/ )  ||
|    /\    ||
|          ||
|         J|'
 ``````````  
"""},
  38 : {
    "rank"  :12,
    "suit"  :"Clubs",
    "black_jack_score"  :10,
    "image" :r"""
.::::::::::::
|Q         ||
|          ||
|    __    ||
|   (  )   ||
|  ( \/ )  ||
|    /\    ||
|          ||
|         Q|'
 ``````````  
"""},
  39 : {
    "rank"  :13,
    "suit"  :"Clubs",
    "black_jack_score"  :10,
    "image" :r"""
.::::::::::::
|K         ||
|          ||
|    __    ||
|   (  )   ||
|  ( \/ )  ||
|    /\    ||
|          ||
|         K|'
 ``````````  
"""},
  40 : {
    "rank"  :1,
    "suit"  :"Spades",
    "black_jack_score"  :11,
    "image" :r"""
.::::::::::::
|A         ||
|          ||
|    /\    ||
|   //\\   ||
|  ((()))  ||
|    /\    ||
|          ||
|         X|'
 ``````````  
"""},
  41 : {
    "rank"  :2,
    "suit"  :"Spades",
    "black_jack_score"  :2,
    "image" :r"""
.::::::::::::
|2         ||
|          ||
|    /\    ||
|   //\\   ||
|  ((()))  ||
|    /\    ||
|          ||
|         2|'
 ``````````  
"""},
  42 : {
    "rank"  :3,
    "suit"  :"Spades",
    "black_jack_score"  :3,
    "image" :r"""
.::::::::::::
|3         ||
|          ||
|    /\    ||
|   //\\   ||
|  ((()))  ||
|    /\    ||
|          ||
|         3|'
 ``````````  
"""},
  43 : {
    "rank"  :4,
    "suit"  :"Spades",
    "black_jack_score"  :4,
    "image" :r"""
.::::::::::::
|4         ||
|          ||
|    /\    ||
|   //\\   ||
|  ((()))  ||
|    /\    ||
|          ||
|         4|'
 ``````````  
"""},
  44 : {
    "rank"  :5,
    "suit"  :"Spades",
    "black_jack_score"  :5,
    "image" :r"""
.::::::::::::
|5         ||
|          ||
|    /\    ||
|   //\\   ||
|  ((()))  ||
|    /\    ||
|          ||
|         5|'
 ``````````  
"""},
  45 : {
    "rank"  :6,
    "suit"  :"Spades",
    "black_jack_score"  :6,
    "image" :r"""
.::::::::::::
|6         ||
|          ||
|    /\    ||
|   //\\   ||
|  ((()))  ||
|    /\    ||
|          ||
|         6|'
 ``````````  
"""},
  46 : {
    "rank"  :7,
    "suit"  :"Spades",
    "black_jack_score"  :7,
    "image" :r"""
.::::::::::::
|7         ||
|          ||
|    /\    ||
|   //\\   ||
|  ((()))  ||
|    /\    ||
|          ||
|         7|'
 ``````````  
"""},
  47 : {
    "rank"  :8,
    "suit"  :"Spades",
    "black_jack_score"  :8,
    "image" :r"""
.::::::::::::
|8         ||
|          ||
|    /\    ||
|   //\\   ||
|  ((()))  ||
|    /\    ||
|          ||
|         8|'
 ``````````  
"""},
  48 : {
    "rank"  :9,
    "suit"  :"Spades",
    "black_jack_score"  :9,
    "image" :r"""
.::::::::::::
|9         ||
|          ||
|    /\    ||
|   //\\   ||
|  ((()))  ||
|    /\    ||
|          ||
|         9|'
 ``````````  
"""},
  49 : {
    "rank"  :10,
    "suit"  :"Spades",
    "black_jack_score"  :10,
    "image" :r"""
.::::::::::::
|10        ||
|          ||
|    /\    ||
|   //\\   ||
|  ((()))  ||
|    /\    ||
|          ||
|        10|'
 ``````````  
"""},
  50 : {
    "rank"  :11,
    "suit"  :"Spades",
    "black_jack_score"  :10,
    "image" :r"""
.::::::::::::
|J         ||
|          ||
|    /\    ||
|   //\\   ||
|  ((()))  ||
|    /\    ||
|          ||
|         J|'
 ``````````  
"""},
  51 : {
    "rank"  :12,
    "suit"  :"Spades",
    "black_jack_score"  :10,
    "image" :r"""
.::::::::::::
|Q         ||
|          ||
|    /\    ||
|   //\\   ||
|  ((()))  ||
|    /\    ||
|          ||
|         Q|'
 ``````````  
"""},
  52 : {
    "rank"  :13,
    "suit"  :"Spades",
    "black_jack_score"  :10,
    "image" :r"""
.::::::::::::
|K         ||
|          ||
|    /\    ||
|   //\\   ||
|  ((()))  ||
|    /\    ||
|          ||
|         K|'
 ``````````  
"""},
  53 : {
    "rank"  :99,
    "suit"  :"CardBack",
    "black_jack_score"  :99,
    "image" :r"""
.::::::::::::
| ________ ||
||\/\/\/\/|||
||/\/\/\/\|||
||\/\/\/\/|||
||/\/\/\/\|||
||\/\/\/\/|||
||/\/\/\/\|||
|''''''''''|'
 ``````````  
"""},
  54 : {
    "rank"  :99,
    "suit"  :"CardBack",
    "black_jack_score"  :99,
    "image" :r"""
.::::::::::::
| ________ ||
||\\//\\//|||
||//\\//\\|||
||\\//\\//|||
||//\\//\\|||
||\\//\\//|||
||//\\//\\|||
|''''''''''|'
 ``````````  
"""},
  55 : {
    "rank"  :99,
    "suit"  :"CardBack",
    "black_jack_score"  :99,
    "image" :r"""
.::::::::::::
| ________ ||
|| | | | ||||
||| | | | |||
|| | | | ||||
||| | | | |||
|| | | | ||||
||| | | | |||
|''''''''''|'
 ``````````  
"""},
  56 : {
    "rank"  :99,
    "suit"  :"CardBack",
    "black_jack_score"  :99,
    "image" :r"""
.::::::::::::
| ________ ||
|| \ \ / /|||
||/ / \ \ |||
|| \ \ / /|||
||/ / \ \ |||
|| \ \ / /|||
||/ / \ \ |||
|''''''''''|'
 ``````````  
"""},
  57 : {
    "rank"  :99,
    "suit"  :"DeckBack",
    "black_jack_score"  :99,
    "image" :r"""
  ___________
.'_________.'|
| ________ | |
||\/\/\/\/|| |
||/\/\/\/\|| |
||\/\/\/\/|| |
||/\/\/\/\|| |
||\/\/\/\/|| |
||/\/\/\/\|| |
|''''''''''|,'
 ``````````  
"""},
  58 : {
    "rank"  :99,
    "suit"  :"DeckBack",
    "black_jack_score"  :99,
    "image" :r"""
  ___________
.'_________.'|
| ________ | |
||\\//\\//|| |
||//\\//\\|| |
||\\//\\//|| |
||//\\//\\|| |
||\\//\\//|| |
||//\\//\\|| |
|''''''''''|,'
 ``````````  
"""},
  59 : {
    "rank"  :99,
    "suit"  :"DeckBack",
    "black_jack_score"  :99,
    "image" :r"""
  ___________
.'_________.'|
| ________ | |
|| | | | ||| |
||| | | | || |
|| | | | ||| |
||| | | | || |
|| | | | ||| |
||| | | | || |
|''''''''''|,'
 ``````````  
"""},
  60 : {
    "rank"  :99,
    "suit"  :"DeckBack",
    "black_jack_score"  :99,
    "image" :r"""
  ___________
.'_________.'|
| ________ | |
|| \ \ / /|| |
||/ / \ \ || |
|| \ \ / /|| |
||/ / \ \ || |
|| \ \ / /|| |
||/ / \ \ || |
|''''''''''|,'
 ``````````  
"""}
}


def render_cards_from_list(cardlist):
    """
    Renders cards to the screen
    """
    card_array = []
    for card_dex in range(len(cardlist)):
        this_list = cardlist[card_dex]["image"].splitlines()
        card_array.append(this_list)
        
    if card_array[0][1] != "":
        cal = len(card_array)
        if cal <= 4:
            for line_dex in range(len(card_array[0])):
                if line_dex == 0:
                    continue
                for card_dex in range(cal):
                        print(card_array[card_dex][line_dex]+"    ",end="")
                print("")
        else:
            for line_dex in range(len(card_array[0])):
                if line_dex == 0:
                    continue
                for card_dex in range(4):
                        print(card_array[card_dex][line_dex]+"    ",end="")
                print("")
                    
            for line_dex in range(len(card_array[0])):
                if line_dex == 0:
                    continue
                for card_dex in range(4,cal):
                        print(card_array[card_dex][line_dex]+"    ",end="")
                print("")


def deal_card():
    """
    Deals one card.
    """
    return DECK_DICT[random.randint(1, 52)]


def calculate_score(hand_list):
    """
    calculates the point value of a given blackjack hand.
    """
    hand = []
    for each in range(len(hand_list)):
        hand.append(hand_list[each]["black_jack_score"])
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
    if sum(hand) == 21 and len(hand) == 2:
        return 0
    else:
        return sum(hand)


def compare_hands(user_score, dealer_score):
    """
    Compares Hands
    """
    if user_score > 21 and dealer_score > 21:
        return "You Busted!!!!!!"
    elif user_score == dealer_score:
        return "Push"
    elif dealer_score == 0:
        return "Dealer Hit BlackJack. YOU LOSE!!!!"
    elif user_score == 0:
        return "You Hit BlackJack. YOU WIN!!!!"
    elif user_score > 21:
        return "You Busted!!!!!!"
    elif dealer_score > 21:
        return "Dealer Busted! YOU WIN!!!!"
    elif user_score > dealer_score:
        return "YOU WIN!!!!"
    elif dealer_score > user_score:
        return "YOU LOSE!!!!"


def run_game():
    """
    Run a new game to completion
    """
    user_cards = []
    dealer_cards = []
    for _ in range(2):
        user_cards.append(deal_card())
        dealer_cards.append(deal_card())
    game_over = False
    while not game_over:
        user_score = calculate_score(user_cards)
        dealer_score = calculate_score(dealer_cards)

        print("\n"*80)
        print("The Dealer is showing:")
        print("")
        temp_dealers_cards = [dealer_cards[0],DECK_DICT[54]]
        render_cards_from_list(temp_dealers_cards)
        print("\n\n\n\n")
        print(f"Your Hand Scores: {user_score}")
        render_cards_from_list(user_cards)
        if dealer_score == 0 or user_score == 0 or user_score > 21:
            game_over = True
        else:
            hit_or_stay = input("Hit or stay?(h,s): ")
            if hit_or_stay == 'h':
                user_cards.append(deal_card())
                user_score = calculate_score(user_cards)
            else:
                game_over = True

                while dealer_score < 17 and dealer_score != 0:
                    dealer_cards.append(deal_card())
                    dealer_score = calculate_score(dealer_cards)
    print("\n"*80)
    print(f"Dealer's Final Score is: {dealer_score}")
    print("Dealer's Final Hand is:")
    print("")
    render_cards_from_list(dealer_cards)
    print("\n\n")
    print(f"Your Hand Scores: {user_score}")
    print("")
    render_cards_from_list(user_cards)
    print(compare_hands(user_score, dealer_score))


if __name__=="__main__":

    print(TITLE)
    while input("\nWould you like to start a new game? (y,n): ").lower() == 'y':
        run_game()
