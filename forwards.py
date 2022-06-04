#!/usr/bin/env python3

### IMPORT STATEMENTS ###
import sys


### HELPER FUNCTIONS (IF NECESSARY) ###
def forwards_is_backwards(file):
  # for i in range(0, int(len(file)/2)):
  #   if file[i] != file[len(file-i-1)]:
  #     return False

  # return True  

  for i in file:
    i = i.strip()
    reverse_i = i[::-1]
    print(i == reverse_i)

### MAIN FUNCTION ###
def main():
  file_name = sys.argv[1]
  with open(file_name) as f:
    forwards_is_backwards(f)
  
  
### DUNDER CHECK ###
if __name__ == "__main__":
  main()
