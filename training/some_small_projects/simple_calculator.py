def add (x,y):
    return x + y
def subtr(x,y):
    return x - y
def multpl(x,y):
    return x * y 
def divide(x,y):
    return x / y
print("select the operation: ")
print("+: add ")
print("-: subtract ")
print("*: multiply ")
print("/: divide ")
try:
    while True:
        choice = input("Make your choice: \n")
        if choice in ("+", "-", "*", "/"):
            num1 = float(input("enter the first num: \n"))
            num2 = float(input("enter the second num: \n"))
            if choice == "+":
                print(num1, "+", num2 , "=" , add(num1, num2))
            elif choice == "-":
                print(num1, "-", num2 , "=" , subtr(num1, num2))
            elif choice == "*":
                print(num1, "*", num2 , "=" , multpl(num1, num2))
            elif choice == "/":
                print(num1, "/", num2 , "=" , divide(num1, num2))
            
            next_calculation = input("should we do further calc? (yes/no)").lower()
            if next_calculation == "no":
                break
        else:
            print("invalid input")

except:
    print("wrong choice, try again")