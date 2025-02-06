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