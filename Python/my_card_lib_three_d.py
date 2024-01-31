#!/bin/python3
"""Makin a deck of 3d cards"""

# DECK = ["""
#   ___________
# .'_________.'|
# |X         | |
# |          | |
# |    /\    | |
# |   /  \   | |
# |   \  /   | |
# |    \/    | |
# |          | |
# |         X|,'
#  ``````````
# ""","""
#   ___________
# .'_________.'|
# |X         | |
# |   _  _   | |
# |  ( \/ )  | |
# |   \  /   | |
# |    \/    | |
# |          | |
# |          | |
# |         X|,'
#  ``````````
# ""","""
#   ___________
# .'_________.'|
# |X         | |
# |          | |
# |    __    | |
# |   (  )   | |
# |  ( \/ )  | |
# |    /\    | |
# |          | |
# |         X|,'
#  ``````````
# ""","""
#   ___________
# .'_________.'|
# |X         | |
# |          | |
# |    /\    | |
# |   //\\\\   | |
# |  ((()))  | |
# |    /\    | |
# |          | |
# |         X|,'
#  ``````````
#  ""","""
#   ___________
# .'_________.'|
# | ________ | |
# ||\/\/\/\/|| |
# ||/\/\/\/\|| |
# ||\/\/\/\/|| |
# ||/\/\/\/\|| |
# ||\/\/\/\/|| |
# ||/\/\/\/\|| |
# |''''''''''|,'
#  ``````````
# ""","""
#   ___________
# .'_________.'|
# | ________ | |
# ||\\//\\//|| |
# ||//\\//\\|| |
# ||\\//\\//|| |
# ||//\\//\\|| |
# ||\\//\\//|| |
# ||//\\//\\|| |
# |''''''''''|,'
#  ``````````
# ""","""
#   ___________
# .'_________.'|
# | ________ | |
# || | | | ||| |
# ||| | | | || |
# || | | | ||| |
# ||| | | | || |
# || | | | ||| |
# ||| | | | || |
# |''''''''''|,'
#  ``````````
# ""","""
#   ___________
# .'_________.'|
# | ________ | |
# || \ \ / /|| |
# ||/ / \ \ || |
# || \ \ / /|| |
# ||/ / \ \ || |
# || \ \ / /|| |
# ||/ / \ \ || |
# |''''''''''|,'
#  ``````````
# """]


DECK = ["""
.::::::::::::
|X         ||
|          ||
|    /\    ||
|   /  \   ||
|   \  /   ||
|    \/    ||
|          ||
|         X|'
 ``````````
""",
"""
.::::::::::::
|X         ||
|   _  _   ||
|  ( \/ )  ||
|   \  /   ||
|    \/    ||
|          ||
|          ||
|         X|'
 ``````````
""",
"""
.::::::::::::
|X         ||
|          ||
|    __    ||
|   (  )   ||
|  ( \/ )  ||
|    /\    ||
|          ||
|         X|'
 ``````````
""",
"""
.::::::::::::
|X         ||
|          ||
|    /\    ||
|   //\\\\   ||
|  ((()))  ||
|    /\    ||
|          ||
|         X|'
 ``````````
"""]


test = """
  ___________
.'_________.'|
|X         | |
|   _  _   | |
|  ( \/ )  | |
|   \  /   | |
|    \/    | |
|          | |
|          | |
|         X|,'
 ``````````
""","""
  ___________
.'_________.'|
|X         | |
|          | |
|    __    | |
|   (  )   | |
|  ( \/ )  | |
|    /\    | |
|          | |
|         X|,'
 ``````````
""","""
  ___________
.'_________.'|
|X         | |
|          | |
|    /\    | |
|   //\\\\   | |
|  ((()))  | |
|    /\    | |
|          | |
|         X|,'
 ``````````
 """













# DECK_DICT = {}
    
# for each in range(len(DECK)):
#     DECK_DICT[each] = DECK[each]

# for each in range(52):
#     print(DECK_DICT[each])

# import json

# # Convert and write JSON object to file
# with open("myDeck.json", "w") as outfile: 
#     json.dump(DECK_DICT, outfile, indent=4)

# CARD_BACKS_DICT = {}
    
# for each in range(len(CARD_BACKS)):
#     CARD_BACKS[each] = CARD_BACKS[each]

# for each in range(5):
#     print(CARD_BACKS[each])

# import json

# # Convert and write JSON object to file
# with open("myCardBacks.json", "w") as outfile: 
#     json.dump(CARD_BACKS, outfile, indent=4)

# card1 = DECK[0]
# card2 = DECK[1]
# card1Arr = card1.splitlines()
# card2Arr = card2.splitlines()



# for each in DECK:
#     print("\n"+each+"\n")
# print(len(DECK))

mdex = 0

card1Arr = DECK[mdex].splitlines()
card2Arr = DECK[mdex+1].splitlines()
card3Arr = DECK[mdex+2].splitlines()
card4Arr = DECK[mdex+3].splitlines()

for each in range(len(card1Arr)):
    if each == 1:
        print(card1Arr[each]+"    "+card2Arr[each]+"    "+card3Arr[each]+"    "+card4Arr[each])
    elif each == len(card1Arr)-1:
        print(card1Arr[each]+"      "+card2Arr[each]+"      "+card3Arr[each]+"      "+card4Arr[each])
    
    
    else:
        print(card1Arr[each]+"    "+card2Arr[each]+"    "+card3Arr[each]+"    "+card4Arr[each]) 







# mdex = 0

# card1Arr = DECK[mdex].splitlines()
# card2Arr = DECK[mdex+1].splitlines()
# card3Arr = DECK[mdex+2].splitlines()
# card4Arr = DECK[mdex+3].splitlines()

# for each in range(len(card1Arr)):
#     if each == 1:
#         print(card1Arr[each]+"     "+card2Arr[each]+"     "+card3Arr[each]+"     "+card4Arr[each])
#     elif each == len(card1Arr)-1:
#         print(card1Arr[each]+"       "+card2Arr[each]+"       "+card3Arr[each]+"       "+card4Arr[each])
    
    
#     else:
#         print(card1Arr[each]+"    "+card2Arr[each]+"    "+card3Arr[each]+"    "+card4Arr[each]) 


# def render_4_cards(mdex, DECK):
    
#     card1Arr = DECK[mdex].splitlines()
#     card2Arr = DECK[mdex+1].splitlines()
#     card3Arr = DECK[mdex+2].splitlines()
#     card4Arr = DECK[mdex+3].splitlines()

#     for each in range(len(card1Arr)):
#         if each == len(card1Arr)-1 or each == 1:
#             print(card1Arr[each]+"     "+card2Arr[each]+"     "+card3Arr[each]+"     "+card4Arr[each])
#         else:
#             print(card1Arr[each]+"    "+card2Arr[each]+"    "+card3Arr[each]+"    "+card4Arr[each]) 

# for each in range(0,52,4):
#     render_4_cards(each, DECK)