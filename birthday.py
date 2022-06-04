#!/usr/bin/env python3

### IMPORT STATEMENTS ###
import sys




### HELPER FUNCTIONS (IF NECESSARY) ###
def birthday_party(names):
  k = {
    "David": 0,
    "Llana": 0,
    "Lily": 0,
    "Corey": 0,
    "Elaine": 0,
  }
  for j in names.readlines():
    if j == "David":
      k["David"] += 1
    elif j == "Llana":
      k["Llana"] += 1
    elif j == "Lily":
      k["Lily"] += 1
    elif j == "Corey":
      k["Corey"] += 1
    elif j == "Elaine":
      k["Elaine"] += 1
  return("Corey - {}\nDavid - {}\nElaine - {}\nLily - {}\nLlana - {}".format(k["Corey"],k["David"],k["Elaine"],k["Lily"],k["Llana"]))


### MAIN FUNCTION ###
def main():
 file_name = sys.argv[1]
 open_file = open(file_name)
 print(birthday_party(open_file))
 open_file.close()
  

### DUNDER CHECK ###
if __name__ == "__main__":
  main()
