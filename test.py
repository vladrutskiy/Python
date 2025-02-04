print("hello, I'm going to ask you to print two numbers…")
# print("I hope you are OK with that")
# x = input("Please enter first number: ")
# y = input("Please enter second number: ")
# third_num = input("Please enter third number: ")
# print(type(y))
# print(type(x))
# print(type(third_num))
# newX = int(x)
# newY = int(y)
# new_third_num = int(third_num)
# print(type(newX))
# print(type(newY))
# print(type(new_third_num))
# z = newX + newY
# w = newX * newY
# square_root_of_third_num = new_third_num ** 0.5
# print("I added both numbers, and the result is: ", z)
# print("I multiplied both numbers, and the result is: ", w)
# print("the square root of third number is " , square_root_of_third_num)

# I'll try to make the code les repetitive
def calculation ():
    num1 = int(input("Please enter first number: "))
    num2 = int(input("Please enter second number: "))
    num3 = int(input("Please enter thisrd number: "))
    add_two_nums = num1 + num2
    mult_two_nums= num1 * num2
    sqr_rt_num1 = num1 ** 0.5
    sqr_rt_num2 = num2 ** 0.5
    triang_S = (num1 + num2 + num3 ) / 2
    triang_A = (triang_S * ((triang_S - num1) * (triang_S - num2) * (triang_S - num3))) ** 0.5
    print("the sum of two numbers is: ", add_two_nums)
    print("if multiply the two numbers the result is: " , mult_two_nums)
    print("the square root of the first number is: " , sqr_rt_num1)
    print("the square root of the second number is: " , sqr_rt_num2)
    print("If the triangle sides are: a = %i, b = %i, c = %i then it's area is %f " %(num1, num2, num3, triang_A))

calculation()

# interesting way to swap two numbers
x = 5
y = 3
swap = x
x = y 
y = swap
print(x, y)

# a login like function
attempt = 0
max_attempt = 5
def login (username, password):
    user = input("Please enter username: ").lower
    passs = input("Please enter the password: ").lower

    if user == (username) and passs == (password):
        return True
    return False
while True :
    if login("rory", "goal"):
        print("The login is successful!")
        break
    attempt += 1
    if attempt >= max_attempt:
        print("something went wrong")
        break
    print("The user name or password are incorrect \n")