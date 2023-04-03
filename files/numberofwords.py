"""This is a python program that opens a file and reads the content and the return 
is the total number of words in the file"""


file_name = input("Enter the name of the file you want to open: ")

with open(file_name, 'r') as file:
    content = file.read()
    words = len(content.split())

print("The file contains", words , "words")
