"""Json is a data structure that is used to store and exchange data
uses JavaScript notation

for one to use json one must import json module

to convert json to python dictionary we use .loads() function
to convert python to json string we use .dumps() function"""

#importing the json module
import json

x = {"name" : "John", "Age" : "20", "Course" : "BSCIT"} #a dictionary in python

m = '{"name" : "Samuel", "Age" : "21", "Course" : "BSCIT"  }'

y = json.dumps(x, indent = 4) #converting the dictionary that is represented by the variable x to ajson format

n = json.loads(m)  #converting the json string to a python dictionary

print(y)  #this will print the values as a json string

print(n)   #this will print the values as python dictionary





