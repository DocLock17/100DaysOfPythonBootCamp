#!/bin/python3
"""
# #### NOTE ####
# Here I am attaching my best debugging notes since they are a bit more 
# advanced than the instructors exercise 
"""

#### Logging:
import logging


# An indication that something unexpected happened, or
# that a problem might occur in the near future
# (e.g. ‘disk space low’).
# The software is still working as expected.
logging.warning('WARNING')
logging.log(30, 'WARNING')

# Due to a more serious problem, the software has not been able to perform some function.
logging.error('ERROR')
logging.log(40, 'ERROR')

# A serious error, indicating that the program itself may be unable to continue running.
logging.critical('CRITICAL')
logging.log(50, 'CRITICAL')

DEBUG = True
# DEBUG = False
# if DEBUG:breakpoint()

# #### You can also invoke pdb from the command line to debug other scripts. For example:
# #$ python3 -m pdb myscript.py
# Then:
# ####>step <-- Walk step forward
# ####>list <-- Shows area snippet
# ####>b $n <-- Add breakpoint to line($n)
# ####>q <-- Exit

X = 10
for each in range(0, X):
    if DEBUG:
        breakpoint()
    print(each)
