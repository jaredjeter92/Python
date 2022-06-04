
#!/usr/bin/env python3


### IMPORT STATEMENTS ###
def ip_counter(file):
  ip_list = []
  ip_dict = {}
  pat = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
  for x in file:
    ip_list.append(pat.search(x)[0])
  for x in ip_list:
    ip_dict[x] = ip_dict.get(x,0) + 1
  result = ""
  for key, value in sorted(ip_dict.items()):
    result += key + " - " + str(value) + "\n"
 
 
  return result.strip()
### MAIN FUNCTION ###
def main():
 x = sys.argv[1]
with open(x) as f:
    print(ip_counter(f))
 f.close()


### DUNDER CHECK ###





