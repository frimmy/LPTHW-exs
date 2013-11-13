#imports from the python system the argv class/features/modules
from sys import argv

#defines two arguments entered on the CL
script, filename = argv

#defines txt as the file name enetered on the CL and
# assigns the txt obj to the variable 'text'
txt = open(filename)

# prints a line and the filename entered on the CL
print "Here's your file %r:" % filename
#prints the txt file out 
print txt.read()

#prints an instruction
print "Type the filename again:"

#assings user input of file name to variable 'file_again'
file_again = raw_input("> ")

# assigns the opened txt file to 'txt_again' variable 
txt_again = open(file_again)

# prints a read file to CL
print txt_again.read()
txt.close()
txt_again.close()
