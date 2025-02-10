# we can use zip function to go through several lists at the same time
keys = ["book", "author","genre", "year"]
values = ["one", "unknown", "mystery", "2020"]
numbers = ["1", "2", "3", "4"]
for k,v,n in zip (keys, values, numbers):
    print(k, "goes for ", v, "and here goes a number", n)
