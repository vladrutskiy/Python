# we will do this with the help of modules
# it will be module random
# to install it you need to use terminal with a command  pip install random

# lets's try to write a program that asks the user to guess the random number
import random
guess_num = (random.randint(0,10))
guesses = 0
max_guesses = 3

while guesses < max_guesses:
    the_num = int(input("Please enter a number from 0 to 10\n"))
    if the_num == guess_num:
        print(" you are correct the number is ", guess_num)
        break
    else:
        print("please try again")
    guesses += 1
    if guesses == max_guesses:
        print("you lose, the number was", guess_num)
    
        

