"""This is a python program that once it is run :- 
 -it will prompt you to enter the name you wish to give to your file,
 -create the file with the name you have given it ,
-prompt you to enter the content that you want to be displayed, and
immediately you will see a new file that will be created.
Check the file to see whether the contents you entered are there"""

file_name = input("Enter the name you wish to give to your file : ")
contents = input("Enter the content that you wish to be displayed : ")


def python_files(file_name , contents):
    f = open(file_name + ".txt", "w" )
    f.write(contents) 
    f.close()

    f = open(file_name + ".txt", "r")
    print(f.read())  

print("This is the infromation in the file")    

python_files(file_name, contents)    


print(" Yaay a new file has been created !! ")

    
    

