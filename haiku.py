```python
#!/usr/bin/env python3

### IMPORT STATEMENTS ###
import sys




### HELPER FUNCTIONS (IF NECESSARY) ###
def haiku(dict):
  input = direct.read()
  haiku_dct = ast.literal_eval(input)
  return_str = ""
  haiku_1 = len(haiku_dct)

  for num in range(1, haiku_l):
    return _str += haiku_dct[str(num)]
    if haiku_dct[str(num)] != "\n" and num != haiku_l - 1:
      return _str += ""
    elif haiku_dct[str(num)] == "\n":
      return_str = return _str.rstrip() + "\n"
  
  return return_str




### MAIN FUNCTION ###
def main():
file_name = sys.argv[1]
with open (file_name) as f:
  print (haiku(f))
  


### DUNDER CHECK ###
if __name__ == "__main__":
 main()
