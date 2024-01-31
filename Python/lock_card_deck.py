#!/bin/python3
"""Makin a deck of 3d cards"""

def mctesty():
      print('import worked')

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

# for each in range(1, 61):
#     print(DECK_DICT[each]["rank"])
#     print(DECK_DICT[each]["suit"])
#     print(DECK_DICT[each]["black_jack_score"])
#     print(DECK_DICT[each]["image"])



def render_cards(card1=0, card2=0, card3=0, card4=0, card5=0, card6=0, card7=0, card8=0):
      
    if card1 != 0:
      card1Arr = DECK_DICT[card1]["image"].splitlines()
    else:
          card1Arr = ["","","","","","","","","","",""]
    if card2 != 0:
      card2Arr = DECK_DICT[card2]["image"].splitlines()
    else:
      card2Arr = ["","","","","","","","","","",""]
    if card3 != 0:
      card3Arr = DECK_DICT[card3]["image"].splitlines()
    else:
      card3Arr = ["","","","","","","","","","",""]
    if card4 != 0:
      card4Arr = DECK_DICT[card4]["image"].splitlines()
    else:
      card4Arr = ["","","","","","","","","","",""]


    if card5 != 0:
          card5Arr = DECK_DICT[card5]["image"].splitlines()
    else:
      card5Arr = ["","","","","","","","","","",""]
    if card6 != 0:
          card6Arr = DECK_DICT[card6]["image"].splitlines()
    else:
      card6Arr = ["","","","","","","","","","",""]
    if card7 != 0:
          card7Arr = DECK_DICT[card7]["image"].splitlines()
    else:
      card7Arr = ["","","","","","","","","","",""]
    if card8 != 0:
          card8Arr = DECK_DICT[card8]["image"].splitlines()
    else:
      card8Arr = ["","","","","","","","","","",""]     
      
    if card1Arr[1] != "": 
      for each in range(len(card1Arr)):
          if each == 0:
              continue
          if each == 1:
              print(card1Arr[each]+"    "+card2Arr[each]+"    "+card3Arr[each]+"    "+card4Arr[each])
          elif each == len(card1Arr)-1:
              print(card1Arr[each]+"      "+card2Arr[each]+"      "+card3Arr[each]+"      "+card4Arr[each])
          else:
              print(card1Arr[each]+"    "+card2Arr[each]+"    "+card3Arr[each]+"    "+card4Arr[each]) 

    if card5Arr[1] != "":
      for each in range(len(card1Arr)):
          if each == 0:
              continue
          if each == 1:
              print(card5Arr[each]+"    "+card6Arr[each]+"    "+card7Arr[each]+"    "+card8Arr[each])
          elif each == len(card1Arr)-1:
              print(card5Arr[each]+"      "+card6Arr[each]+"      "+card7Arr[each]+"      "+card8Arr[each])
          else:
              print(card5Arr[each]+"    "+card6Arr[each]+"    "+card7Arr[each]+"    "+card8Arr[each]) 


def render_cards_from_list(cardlist):
      
      # print(type(cardlist))
      # print(type(cardlist[0]))
      # print(type(cardlist[0]["image"]))
      # print(len(cardlist))
      # print(len(cardlist[0]))
      # print(len(cardlist[0]["image"]))
      
      card_array = []
      for card_dex in range(len(cardlist)):
            # print(card_dex)
            # print(cardlist[card_dex]["image"])
            this_list = cardlist[card_dex]["image"].splitlines()
            # print(this_list)
            card_array.append(this_list)
            # card_array[card_dex] += this_list
            # print(card_array)
            
      if card_array[0][1] != "":
          # print(len(card_array[0]))
          cal = len(card_array)
          if cal <= 4:
            for line_dex in range(len(card_array[0])):
                # print(line_dex)
                if line_dex == 0:
                    continue
                else:
                  # print(len(card_array))
                    for card_dex in range(cal):
                          print(card_array[card_dex][line_dex]+"    ",end="")
                    print("")
          else:
            for line_dex in range(len(card_array[0])):
                # print(line_dex)
                if line_dex == 0:
                    continue
                else:
                    for card_dex in range(4):
                          print(card_array[card_dex][line_dex]+"    ",end="")
                    print("")
                    
            for line_dex in range(len(card_array[0])):
                # print(line_dex)
                if line_dex == 0:
                    continue
                else:
                    for card_dex in range(4,cal):
                          print(card_array[card_dex][line_dex]+"    ",end="")
                    print("")
                    

# render_cards(32,54)
# render_cards(44,23)

# print("Test 1")
# render_cards(32,54)
# print("Test 2")
# render_cards(44,23,8)
# print("Test 3")
# render_cards(48,27,4,31,19)
# print("Test 4")
# render_cards(2,3,17,38,51,22,12,9)

