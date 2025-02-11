lower = int(input("please enter the lower number \n"))
upper = int(input("please enter the higher number \n"))
print("prime number(s) between", lower, "and", upper, "is (are): ")
for num in range(lower, upper + 1 ):
    if num > 1:
        for i in range (2, num):
            if (num % i) == 0:
                break
        else:
            print(num)