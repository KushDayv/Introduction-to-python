"""RegEx is a short for regular expression. this is used to form a search parttern
This is like checking if there is a certain set of characters from a givent string/set of data"""

import re

txt = "The weather today is Cloudy"

x = re.search("weather",txt)  #this will check for the presence of the word weather from the statement
y = re.findall("e",txt) #finds all the letter e from the statement 

if x:
    print("The word is present in the statement")
else:
    print("There's no Match") #this will print either true of false depending on the output

if y:
    print(y)
else:
    print("There's no MATCH")

