# we will do this with the help of modules
# it will be module random
# to install it you need to use terminal with a command  pip install random

# lets's try to write a program that asks the user to guess the random number
import random
guess_num = (random.randint(0,10))
guesses = 0
max_guesses = 3
try:
    while guesses < max_guesses:
        the_num = int(input("\nPlease enter a number from 0 to 10\n"))
        if the_num == guess_num:
            print("You are correct the number is ", guess_num)
            break
        else:
            if the_num > guess_num:
                print("Your number is grater, please try again!")
            else :
                print("Your number is less, please try again.")
        guesses += 1
        if guesses == max_guesses:
            print("You lose, the number was", guess_num)
except: # if user enters letters let's catch this  # noqa: E722
    print("please enter values from the range next time. The game is over. ")
    
        

