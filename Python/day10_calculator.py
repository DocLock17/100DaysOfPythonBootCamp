#!/bin/python3
"""
You can use a string like this or use this raw comment I 
found # pylint: disable=missing-module-docstring
"""

TITLE = """
 _____________________
|  _________________  |
| | CALCULATOR   0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
"""

def calculate(num1,num2,op):
    """ I guess I need docs. """
    if op == '/':
        return num1/num2
    elif op == '+':
        return num1+num2
    elif op == '-':
        return num1-num2
    elif op == '*':
        return num1*num2
    else:
        return 'No Operator Found'

# global continue_flag
CONTINUE_FLAG = 0

while True:
    print(TITLE)
    if CONTINUE_FLAG == 0:
        FIRST_NAME = float(input("What's the first number?: "))
        RESULT = 0
    if CONTINUE_FLAG == 1:
        FIRST_NAME = RESULT
        print("The first number is: "+str(FIRST_NAME))
    operator = input("Pick an Operator: ")
    second_num = float(input("What's the Second number?: "))
    RESULT = calculate(FIRST_NAME,second_num,operator)
    print("\n",FIRST_NAME, " ", operator, " ", second_num, " = ",RESULT,"\n")
    print("Would you like to continue?")
    cont_clear = input("Type 'y' to continue calculating with "+str(RESULT)+", type 'c' \
        to start a new calculation, or type 'n' to quit: ")
    if cont_clear.lower() == 'y':
        # print("This is y")
        CONTINUE_FLAG = 1
    elif cont_clear.lower() == 'c':
        # print("This is c")
        CONTINUE_FLAG = 0
    else:
        # print("This is else")
        break
