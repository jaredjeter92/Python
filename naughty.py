#!/usr/bin/env python3


### IMPORT STATEMENTS ###
import sys




### HELPER FUNCTIONS (IF NECESSARY) ###
def naughty_or_nice(santa_list):
  #santa_list ['good', 'good', 'good', 'bad', 'bad', 'good', 'good', 'good', 'bad', 'good', 'bad', 'good', 'good', 'bad', 'good', 'good', 'bad', 'good', 'bad', 'good', 'good', 'bad', 'good', 'bad', 'bad', 'bad', 'bad', 'bad', 'bad', 'bad', 'bad']
  #good_count = {}
  #for i in santa_list: good_count[i] = good_count.get(i,0)+1
#  santa_list2 = santa_list.read()
 dct = {
   "good": 0,
   "bad": 0,
  }
#  print(santa_list2)
 for y in santa_list.readlines():
  #  print(y)
   good_or_bad = y.split()[-1]
   #print(good_or_bad)
  #  y = y.strip()
  #  y = y.split()[-1]
   if good_or_bad.lower() == "good":
     dct["good"] += 1
   elif good_or_bad.lower() == "bad":
      dct["bad"] += 1
 #print ("Naughty list has [] people!".format(bad))
 #print ("Nice list has [] people!".format(good))
  #  print(bad)
 return("Naughty list has {} people!\nNice list has {} people!".format(dct["bad"],dct["good"]))
#  print("Nice list has {} people!".format(good))


### MAIN FUNCTION ###
def main():
 file_name = sys.argv[1]
  #so the file is imported with sys.argv[1]
 open_file = open(file_name)
#  with open(file_name) as open_file:
 print(naughty_or_nice(open_file))
#print("Naughty list has " + good_count[bad] + " people!" + "\n" + "Nice list has " + good_count[good] + " people!")
  # open_file.close()

### DUNDER CHECK ###
if __name__ == "__main__":
  main()
