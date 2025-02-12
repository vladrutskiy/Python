# this is an import statement that allows us to use statements form another files. here we importing built in Python file
import random

# 
# from random import NV_MAGICCONST

# For loops

books = ["Little woman", "Biology", "Maths", "Hidden figures", "Python codding for dummies"]

for current_book in books:
    print (f"{current_book}, I choose you!")
    print (f"*turning pages sounds* , the {current_book}, book is being processed")
    print (f"{current_book},  the book is read")

print("all books are read!")    


books = ["Language", "Little woman", "Biology", "Maths", "Hidden figures", "Python codding for dummies"]

for current_book in books:
    print (f"{current_book}, I choose you!")
    print (f"*turning pages sounds* , the {current_book}, book is being processed")
    print (f"{current_book},  the book is read")

print("congratulations, all books are read!")    

# While loops
running = True
while running:
   # do some stuff
   print("...still running")
   running = 5 < random.randint(0,10)


# Python don't have "do while statements"
# do:
#    print("something")
#    while (False)

