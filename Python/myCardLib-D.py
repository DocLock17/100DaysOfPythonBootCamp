#!/bin/python3

DECK = ["""
 __________
|A         |
|          |
|    /\\    |
|   //\\\\   |
|   \\\\//   |
|    \\/    |
|          |
|         A|
 ``````````
""","""
 __________
|A         |
|   _  _   |
|  ((\\/))  |
|   \\\\//   |
|    \\/    |
|          |
|          |
|         A|
 ``````````
""","""
 __________
|A         |
|          |
|    __    |
|   (())   |
|  ((\\/))  |
|    /\\    |
|          |
|         A|
 ``````````
""","""
 __________
|A         |
|          |
|    /\\    |
|   //\\\\   |
|  ((\\/))  |
|    /\\    |
|          |
|         A|
 ``````````
""","""
 __________
|K         |
|          |
|    /\\    |
|   //\\\\   |
|   \\\\//   |
|    \\/    |
|          |
|         K|
 ``````````
""","""
 __________
|K         |
|   _  _   |
|  ((\\/))  |
|   \\\\//   |
|    \\/    |
|          |
|          |
|         K|
 ``````````
""","""
 __________
|K         |
|          |
|    __    |
|   (())   |
|  ((\\/))  |
|    /\\    |
|          |
|         K|
 ``````````
""","""
 __________
|K         |
|          |
|    /\\    |
|   //\\\\   |
|  ((\\/))  |
|    /\\    |
|          |
|         K|
 ``````````
""","""
 __________
|Q         |
|          |
|    /\\    |
|   //\\\\   |
|   \\\\//   |
|    \\/    |
|          |
|         Q|
 ``````````
""","""
 __________
|Q         |
|   _  _   |
|  ((\\/))  |
|   \\\\//   |
|    \\/    |
|          |
|          |
|         Q|
 ``````````
""","""
 __________
|Q         |
|          |
|    __    |
|   (())   |
|  ((\\/))  |
|    /\\    |
|          |
|         Q|
 ``````````
""","""
 __________
|Q         |
|          |
|    /\\    |
|   //\\\\   |
|  ((\\/))  |
|    /\\    |
|          |
|         Q|
 ``````````
""","""
 __________
|J         |
|          |
|    /\\    |
|   //\\\\   |
|   \\\\//   |
|    \\/    |
|          |
|         J|
 ``````````
""","""
 __________
|J         |
|   _  _   |
|  ((\\/))  |
|   \\\\//   |
|    \\/    |
|          |
|          |
|         J|
 ``````````
""","""
 __________
|J         |
|          |
|    __    |
|   (())   |
|  ((\\/))  |
|    /\\    |
|          |
|         J|
 ``````````
""","""
 __________
|J         |
|          |
|    /\\    |
|   //\\\\   |
|  ((\\/))  |
|    /\\    |
|          |
|         J|
 ``````````
""","""
 __________
|T         |
|          |
|    /\\    |
|   //\\\\   |
|   \\\\//   |
|    \\/    |
|          |
|         T|
 ``````````
""","""
 __________
|T         |
|   _  _   |
|  ((\\/))  |
|   \\\\//   |
|    \\/    |
|          |
|          |
|         T|
 ``````````
""","""
 __________
|T         |
|          |
|    __    |
|   (())   |
|  ((\\/))  |
|    /\\    |
|          |
|         T|
 ``````````
""","""
 __________
|T         |
|          |
|    /\\    |
|   //\\\\   |
|  ((\\/))  |
|    /\\    |
|          |
|         T|
 ``````````
""","""
 __________
|9         |
|          |
|    /\\    |
|   //\\\\   |
|   \\\\//   |
|    \\/    |
|          |
|         9|
 ``````````
""","""
 __________
|9         |
|   _  _   |
|  ((\\/))  |
|   \\\\//   |
|    \\/    |
|          |
|          |
|         9|
 ``````````
""","""
 __________
|9         |
|          |
|    __    |
|   (())   |
|  ((\\/))  |
|    /\\    |
|          |
|         9|
 ``````````
""","""
 __________
|9         |
|          |
|    /\\    |
|   //\\\\   |
|  ((\\/))  |
|    /\\    |
|          |
|         9|
 ``````````
""","""
 __________
|8         |
|          |
|    /\\    |
|   //\\\\   |
|   \\\\//   |
|    \\/    |
|          |
|         8|
 ``````````
""","""
 __________
|8         |
|   _  _   |
|  ((\\/))  |
|   \\\\//   |
|    \\/    |
|          |
|          |
|         8|
 ``````````
""","""
 __________
|8         |
|          |
|    __    |
|   (())   |
|  ((\\/))  |
|    /\\    |
|          |
|         8|
 ``````````
""","""
 __________
|8         |
|          |
|    /\\    |
|   //\\\\   |
|  ((\\/))  |
|    /\\    |
|          |
|         8|
 ``````````
""","""
 __________
|7         |
|          |
|    /\\    |
|   //\\\\   |
|   \\\\//   |
|    \\/    |
|          |
|         7|
 ``````````
""","""
 __________
|7         |
|   _  _   |
|  ((\\/))  |
|   \\\\//   |
|    \\/    |
|          |
|          |
|         7|
 ``````````
""","""
 __________
|7         |
|          |
|    __    |
|   (())   |
|  ((\\/))  |
|    /\\    |
|          |
|         7|
 ``````````
""","""
 __________
|7         |
|          |
|    /\\    |
|   //\\\\   |
|  ((\\/))  |
|    /\\    |
|          |
|         7|
 ``````````
""","""
 __________
|6         |
|          |
|    /\\    |
|   //\\\\   |
|   \\\\//   |
|    \\/    |
|          |
|         6|
 ``````````
""","""
 __________
|6         |
|   _  _   |
|  ((\\/))  |
|   \\\\//   |
|    \\/    |
|          |
|          |
|         6|
 ``````````
""","""
 __________
|6         |
|          |
|    __    |
|   (())   |
|  ((\\/))  |
|    /\\    |
|          |
|         6|
 ``````````
""","""
 __________
|6         |
|          |
|    /\\    |
|   //\\\\   |
|  ((\\/))  |
|    /\\    |
|          |
|         6|
 ``````````
""","""
 __________
|5         |
|          |
|    /\\    |
|   //\\\\   |
|   \\\\//   |
|    \\/    |
|          |
|         5|
 ``````````
""","""
 __________
|5         |
|   _  _   |
|  ((\\/))  |
|   \\\\//   |
|    \\/    |
|          |
|          |
|         5|
 ``````````
""","""
 __________
|5         |
|          |
|    __    |
|   (())   |
|  ((\\/))  |
|    /\\    |
|          |
|         5|
 ``````````
""","""
 __________
|5         |
|          |
|    /\\    |
|   //\\\\   |
|  ((\\/))  |
|    /\\    |
|          |
|         5|
 ``````````
""","""
 __________
|4         |
|          |
|    /\\    |
|   //\\\\   |
|   \\\\//   |
|    \\/    |
|          |
|         4|
 ``````````
""","""
 __________
|4         |
|   _  _   |
|  ((\\/))  |
|   \\\\//   |
|    \\/    |
|          |
|          |
|         4|
 ``````````
""","""
 __________
|4         |
|          |
|    __    |
|   (())   |
|  ((\\/))  |
|    /\\    |
|          |
|         4|
 ``````````
""","""
 __________
|4         |
|          |
|    /\\    |
|   //\\\\   |
|  ((\\/))  |
|    /\\    |
|          |
|         4|
 ``````````
""","""
 __________
|3         |
|          |
|    /\\    |
|   //\\\\   |
|   \\\\//   |
|    \\/    |
|          |
|         3|
 ``````````
""","""
 __________
|3         |
|   _  _   |
|  ((\\/))  |
|   \\\\//   |
|    \\/    |
|          |
|          |
|         3|
 ``````````
""","""
 __________
|3         |
|          |
|    __    |
|   (())   |
|  ((\\/))  |
|    /\\    |
|          |
|         3|
 ``````````
""","""
 __________
|3         |
|          |
|    /\\    |
|   //\\\\   |
|  ((\\/))  |
|    /\\    |
|          |
|         3|
 ``````````
""","""
 __________
|2         |
|          |
|    /\\    |
|   //\\\\   |
|   \\\\//   |
|    \\/    |
|          |
|         2|
 ``````````
""","""
 __________
|2         |
|   _  _   |
|  ((\\/))  |
|   \\\\//   |
|    \\/    |
|          |
|          |
|         2|
 ``````````
""","""
 __________
|2         |
|          |
|    __    |
|   (())   |
|  ((\\/))  |
|    /\\    |
|          |
|         2|
 ``````````
""","""
 __________
|2         |
|          |
|    /\\    |
|   //\\\\   |
|  ((\\/))  |
|    /\\    |
|          |
|         2|
 ``````````
"""]

CARD_BACKS = ["""
 __________
| ________ |
||\\/\\/\\/\\/||
||/\\/\\/\\/\\||
||\\/\\/\\/\\/||
||/\\/\\/\\/\\||
||\\/\\/\\/\\/||
||/\\/\\/\\/\\||
|''''''''''|
 ``````````
""","""
 __________
| ________ |
||\\\\//\\\\//||
||//\\\\//\\\\||
||\\\\//\\\\//||
||//\\\\//\\\\||
||\\\\//\\\\//||
||//\\\\//\\\\||
|''''''''''|
 ``````````
""","""
 __________
| ________ |
|| | | | |||
||| | | | ||
|| | | | |||
||| | | | ||
|| | | | |||
||| | | | ||
|''''''''''|
 ``````````
""","""
 __________
| ________ |
|| \\ / \\ /||
||/ \\ / \\ ||
|| \\ / \\ /||
||/ \\ / \\ ||
|| \\ / \\ /||
||/ \\ / \\ ||
|''''''''''|
 ``````````
""","""
 __________
| ________ |
|| \\ \\ / /||
||/ / \\ \\ ||
|| \\ \\ / /||
||/ / \\ \\ ||
|| \\ \\ / /||
||/ / \\ \\ ||
|''''''''''|
 ``````````
"""]


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

# card1 = DECK[3]
# card2 = DECK[7]
# card1Arr = card1.splitlines()
# card2Arr = card2.splitlines()



# for each in DECK:
#     print("\n"+each+"\n")
# print(len(DECK))


# mdex = 0

# card1Arr = DECK[mdex].splitlines()
# card2Arr = DECK[mdex+1].splitlines()
# card3Arr = DECK[mdex+2].splitlines()
# card4Arr = DECK[mdex+3].splitlines()

# for each in range(len(card1Arr)):
#     if each == len(card1Arr)-1 or each == 1:
#         print(card1Arr[each]+"     "+card2Arr[each]+"     "+card3Arr[each]+"     "+card4Arr[each])
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





# archive 


# DECK_DICT = {}
    
# for each in range(len(DECK)):
#     DECK_DICT[each] = DECK[each]



# import json

# Convert and write JSON object to file
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

# mdex = 0

# card1Arr = DECK[mdex].splitlines()
# card2Arr = DECK[mdex+1].splitlines()
# card3Arr = DECK[mdex+2].splitlines()
# card4Arr = DECK[mdex+3].splitlines()

# for each in range(len(card1Arr)):
#     if each == 1:
#         print(card1Arr[each]+"    "+card2Arr[each]+"    "+card3Arr[each]+"    "+card4Arr[each])
#     elif each == len(card1Arr)-1:
#         print(card1Arr[each]+"      "+card2Arr[each]+"      "+card3Arr[each]+"      "+card4Arr[each])
    
    
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
