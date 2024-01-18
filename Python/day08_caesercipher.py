#!/bin/bash
"""
Caeser Cipher
"""

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l', \
            'm','n','o','p','q','r','s','t','u','v','w','x', \
            'y','z','A','B','C','D','E','F','G','H','I','J', \
            'K','L','M','N','O','P','Q','R','S','T','U','V', \
            'W','X','Y','Z',' ','-','$','%','?','#','!','@', \
            '&','*','(',')','\'','\"',',','.',';',':','[',']',\
            '{','}','\\','/','|','<','>','+','=','_','^','`', \
            '~','0','1','2','3','4','5','6','7','8','9']

def encrypt(offset, message):
    """
    encrypts message
    """
    encoded = ""
    for each in message:
        encoded += alphabet[(alphabet.index(each)+offset)%len(alphabet)]
    return encoded

def decrypt(offset, message):
    """
    decrypts message
    """
    decoded = ""
    for each in message:
        decoded += alphabet[(alphabet.index(each)-offset)%len(alphabet)]
    return decoded

direction_toggle = input("Encrypt or Decrypt?(e,d): ")
encrypt_offset = int(input("Offset to use: "))
message_string = input("Enter your message: ")

if direction_toggle == 'e':
    print(encrypt(encrypt_offset, message_string))
else:
    print(decrypt(encrypt_offset, message_string))
