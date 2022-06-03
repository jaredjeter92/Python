	#!/usr/bin/env python3
	

	### IMPORT STATEMENTS ###
	import sys
	

	

	

	

	### HELPER FUNCTIONS (IF NECESSARY) ###
	def simple_addition(file):
	  # Write a function called simple_addition with a parameter called file,
	    for line in file:
	      #an open file containing a list of numbers (both ints and floats), two on each line
	        data = line.strip().split()
	      #split the space
	      #Your simple_addition function should add the two numbers together and print their sum (as a float).
	#print the sum
	        print(float(data[0].strip()) + float(data[1].strip()))
	

	

	      
	

	MAIN FUNCTION ###
	def main():
	  # create a variable called `file_name` and set it to the first command line argument (`sys.argv[1]`)
	    if len(sys.argv) > 1:
	        filename = sys.argv[1]
	        try:
	           #Using the `open()` method, open the file and save it as a variable called `open_file`
	            file = open(filename)
	          # Since your simple_addition function is handling the printing
	            simple_addition(file)
	          # Remember to be a responsible programmer and close the `open_file` variable after then function call using the `.close()
	            file.close()
	        except:
	            print(filename + " does not exists!")
	    else:
	        print("Please pass file name as command line argument to the program")
	

	

	      
	

	  
	  
	

	

	### DUNDER CHECK ###
	if __name__ == "__main__":
	  main()
