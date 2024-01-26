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

def deal_card():
    """
    Deals one card.
    """
    cards = [2,3,4,5,6,7,8,9,10,10,10,10,11]
    card = random.choice(cards)
    return card


def calculate_score(hand):
    """
    calculates the point value of a given blackjack hand.
    """
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
        print(f"Your Hand Scores: {user_score}")
        print(f"The Dealer is showing: {dealer_cards[0]}")
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
                print(f"Your Hand Scores: {user_score}")
                print(f"Dealer's Final Hand is: {dealer_score}")
                print(compare_hands(user_score, dealer_score))


if __name__=="__main__":

    print(TITLE)

    while input("\nWould you like to start a new game? (y,n): ").lower() == 'y':
        run_game()
    