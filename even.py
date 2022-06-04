#!/usr/bin/env python3

### IMPORT STATEMENTS ###
import sys


### HELPER FUNCTIONS (IF NECESSARY) ###
def is_even(file):
  for i in file:
    if (int(i) % 2 == 0):
      print(i.strip() + ' ' + str(True))
    else:
      print(i.strip() + ' ' + str(False))


### MAIN FUNCTION ###
def main():
  file_name = sys.argv[1]
  f = open(file_name)
  is_even(f)
  
  


### DUNDER CHECK ###
if __name__ == "__main__":
  main()
