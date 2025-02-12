table_list = (
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10
)

print("Would you see a multiplication table?")
try:
    number = int(input("Please enter a number: \n"))
    for table in table_list:
        result = table * number
        print(table , "by", number, "is", result)
except: 
    print("Your input is incorrect")