# for loop 
# works with lists
numbers = (1,2,3,4,5,6)
for items in numbers:
    print(items)
# work with dictionaries
info = {'name': "Vlad", 'last name': "Rutskyi"}
for key_value in info.keys():
    print(key_value)
for value_value in info.values():
    print(value_value)

# while loops uses conditions for example True and False and it runs loop until condition is not changed.
while True:
    print ("hello")
    break # we need break here to break teh loop and prevent recursion  