#!/usr/bin/env python3

### IMPORT STATEMENTS ###
import sys

### HELPER FUNCTIONS (IF NECESSARY) ###
def lines_lines_lines(file):
  # for line in file:
  #   if "\n" == line:
  #     line2 = line.replace("\n", " ")
  #     print(line2)
  
  return_str = ""
  counter = 0
  str_list = file.readlines()
  # print(str_list)
  for line in str_list:
    counter += 1
    line = line.strip()
    # print(line)
    return_str += line
    if line != "" and counter != len(str_list):
      return_str += " "
  return(return_str)
  




### MAIN FUNCTION ###
def main():
  file_name = sys.argv[1]
  with open (file_name) as f:
    print(lines_lines_lines(f))
  


### DUNDER CHECK ###
if __name__ == "__main__":
  main()
