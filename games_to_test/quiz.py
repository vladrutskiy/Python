print("Welcome to Python quiz app")
play = input("Do you really want to play my Python quiz (Yes/No)? \n")
if play.lower() != "yes":
    print("I've got it. Bye!")
    quit()
score = 0
print("so, let's play! Your score is: ", score)
answer = input("what is 4+4 ?")
if answer == "8":
    score += 1
    print("The answer is correct. \n", "Your score is: ", score )
else:
    score -= 1
    print("Incorrect.  \n", "Your score is: ", score)

answer = input("what is 2+2 ?")
if answer == "4":
    score += 1
    print("The answer is correct. \n", "Your score is: ", score )
else:
    score -= 1
    print("Incorrect.  \n", "Your score is: ", score)

answer = input("what is 8+8 ?")
if answer == "16":
    score += 1
    print("The answer is correct. \n", "Your score is: ", score )
else:
    score -= 1
    print("Incorrect.  \n", "Your score is: ", score)