#!/usr/bin/env python3

### IMPORT STATEMENTS ###
import sys




### HELPER FUNCTIONS (IF NECESSARY) ###
'''match_ends'''
# Write a function called match_ends with a parameter called str_list (list), which represents a list of strings. Your match_ends function should return an int value representing how many strings are both greater than or equal to 2 in length, and have the same char at the beginning and end.

# match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']) returns 3 
# match_ends(['one', 'obo', 'dd', 'dodo', 'agenda']) returns 3
def match_ends(words):
  x = 0
  for word in words:
    if int(len(word)) >= 2 and word[0] == word[-1]:
      x += 1
  return x 



### MAIN FUNCTION ###
arg1 = sys.argv[1:]
print(match_ends(arg1)) 

  
  


### DUNDER CHECK ###
