#!/bin/python3
"""
Password generator
"""

import random

alpha_numeric = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q' \
    ,'r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J' \
    ,'K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Z','0','1','2','3' \
    ,'4','5','6','7','8','9','!','#','$','%','&','*','+','=','-']

print("Welcome to the Password Generator!")

quantity_query = int(input("How long (in characters) should your password be? "))

NEW_SWORD = ''
for each in range(0,quantity_query):
    NEW_SWORD += random.choice(alpha_numeric)
print(NEW_SWORD, end='')
print("")
