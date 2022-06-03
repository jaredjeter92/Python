#!/usr/bin/env python3


### IMPORT STATEMENTS ###
import sys








### HELPER FUNCTIONS (IF NECESSARY) ###
def fix_start(word):
    if len(word) > 0:
        result = ''
        for i in range(len(word)):
            if i > 0 and word[i] == word[0]:
                result += '*'
            else:
                result += word[i]
        return result
    return word














### MAIN FUNCTION ###
def main():
    if len(sys.argv) > 1:
        word = sys.argv[1]
        print(fix_start(word))
   
  
  




### DUNDER CHECK ###
if __name__ == "__main__":
  main(
