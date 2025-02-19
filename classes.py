# example of the basic class




class Example:

    class_variable="hello world!"

    def dance(self): #self is mandatory word in first function of the class 
        print("Dancing starts here")

example = Example()
print(example)
example2 = Example()
print(example2)
print(example.dance)
print(Example.dance) 