def largest_num ():
    while True:    
        try:
            num_1 = int(input("Please enter the first number: \n"))
            num_2 = int(input("Please enter the second number: \n"))
            num_3 = int(input("Please enter the third number: \n"))
            break
        except:  # noqa: E722
            print("Invalid input")
        continue 
    if num_1 > num_2 > num_3:
        print("The ", num_1,  "is larger than ", num_2 , "and", num_3 )
    elif num_2 > num_1 > num_3:
        print("The ", num_2,  "is larger than ", num_1 , "and", num_3 )
    elif num_3 > num_1 > num_2:
        print("The ", num_3,  "is larger than ", num_1 , "and", num_2 )
    elif num_1 == num_2 == num_3:
        print(num_1, "is equal to ", num_2 , " and it is equal to ", num_3)
    else:
        print("There are two equal numbers ")


largest_num()