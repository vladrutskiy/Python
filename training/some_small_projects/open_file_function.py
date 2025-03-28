# to open large file (pdf, xlsx) use pandas
# to open simple files like txt use open() and "r" mode
file =  open("./training/some_small_projects/simple_text_file.txt" , "r")
print(file)
print(file.read())
file.close()

# the write to file function overwrites the old lines ("w" mode)
# file = open("./training/simple_text_file.txt", "w")
# file.write("Hello, I'm adding a new line \n")
# file.close()

# appending the file with new data ("a" mode)
file = open("./training/some_small_projects/simple_text_file.txt", "a")
file.write("No it is me who is adding a new line \n")
file.close()

# to read and write to file use "a+" mode
# .seek function starts reading form the beginning of the file
file = open("./training/some_small_projects/simple_text_file.txt", "a+")
file.seek(0)
print(file.read())
file.write("Me too \n")
file.seek(0)
print(file.read())
file.close()