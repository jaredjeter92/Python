#!/usr/bin/env python3

### IMPORT STATEMENTS ###
import sys




### HELPER FUNCTIONS (IF NECESSARY) ###
'''front_x'''
# Write a function called front_x with a parameter called str_list (list), which represents a list of strings. Your front_x function should return a new list in sorted alphabetical order (ascending), except any string that starts with an x should be listed first (also in alphabetical order). 

# front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']) returns ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']) returns ['xaa', 'xzz', 'axx', 'bbb', 'ccc']

# HINT: consider making 2 lists, sort them correctly, then combine them together



### MAIN FUNCTION ###
def front_x(sl):
  l2 = []
  l = sl.copy()
  l.sort()
  e = len(sl)
  b = (e+1) - e
  while b <= e:
    for i in l:
      if i[0] == "x":
        l2.append(i)
        l.remove(i)
    b += 1
  l2.sort()
  l.sort()
  l4 = l2 + l
  return l4
  
a = sys.argv[1:]
print(front_x(a))
