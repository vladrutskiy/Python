num = int(input("enter a number \n"))
factorial = 1
if num < 0:
    print("The negative numbers don't have factorials")
elif num == 0:
    print("factorial of 0 is 1")
else:
    for  i in range(1, num + 1): #range function prints numbers up to, not including:
        factorial = factorial * i
    print( " the factorial of " , num , "is", factorial)