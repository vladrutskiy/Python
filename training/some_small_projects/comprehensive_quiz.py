# the expandable dictionary of questions "question" : "c_answer"
questions = {
    "4+4": 8,
    "2+2": 4,
    "8+8": 16,
    "5+5": 10,
    "2+7": 9,
    "5+4": 9
}


def check_answers():
    score = 0
    for question, c_answer in  questions.items():
        try:
            print("What is ", question , "? \n")
            answer = int(input("Please enter your answer: \n"))
            if answer == c_answer:
                score += 1
                print("You are correct. Your score is ", score, "\n")
            else :
                score -= 1
                print("The answer is incorrect. Your score is: ", score, "\n")
            if score < 0:
                print("The score is les than 0, you lost.")
                break
        except:  # noqa: E722
            score -= 1
            print("The entered reply isn't in scope. -1 point for you, you have:", score, "points \n")
    print("Congratulations, you ended the quiz, your score is:", score )           
check_answers()