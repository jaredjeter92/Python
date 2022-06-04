#!/usr/bin/env python3

### IMPORT STATEMENTS ###
import sys




### HELPER FUNCTIONS (IF NECESSARY) ###
'''both_ends'''
# Write a function called both_ends with a parameter called s (str), which represents a string. Your both_ends function should return a string made of the first 2 and the last 2 chars of the original string. (ex: 'spring' yields 'spng'). However, if the string length is less than 2, return an empty string instead. 

# both_ends('spring') returns 'spng' 
# both_ends('oogabooga) returns 'ooga'

### MAIN FUNCTION ###
def both_ends(a):
  if len(a) < 2:
    return ""
  elif len(a) >= 2:
    return print (a[0:2] + a[-2:])
  
  


### DUNDER CHECK ###
a = sys.argv[1]
both_ends(a)
