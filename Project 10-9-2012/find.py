#!/usr/bin/env python

# The "import" statement finds modules (whatever those are!) and defines names
# in a namespace (whatever that is!):                                                                          
#                                                                                                              
#   http://docs.python.org/reference/simple_stmts.html#the-import-statement                                    
#                                                                                                              
# The "sys" module provides things related (apparently) to the interpreter
# (whatever that is!):                                                                                         
#                                                                                                              
#   http://docs.python.org/library/sys.html

import sys

USAGE = "Usage: ./find.py word filename [filename]*"

#defining the Fail message? Print both USAGE and Msg if statement FAIL equals True
#sys.exit exits the current Python program.
def fail(msg):
    print >> sys.stderr, USAGE
    print >> sys.stderr, msg
    sys.exit()

#statement used to find word.
try:
    word = sys.argv[1]

#message to show if user doesnt give a word to find.  
except:
    fail("Please provide a word to find.")

#statement used to - 2: starts the list
filenames = sys.argv[2:]
if not filenames:
    fail("Please enter at least one filename.")

#For statement.  For the filename that is given from user from above (filenames) 
#The file name that was open from above is assigned to file_pointer.  If false or error
#IOError, becomes true.  and prints out "Could not open file:" (filename) 
for filename in filenames:
    try:
        file_pointer = open(filename)
    except IOError:
        print >> sys.stderr, "Could not open file:", filename
        continue
#if true, or no errors, program will look for line in such file.
    for line in file_pointer:
        if word in line:
            print filename
            break