import zipfile

def crack_password(password_list, obj):
    test = 0  # Track number of attempts
    with open(password_list, "r") as file:
        for line in file:
            for word in line.split():
                test += 1
                try:
                    obj.extractall(pwd=word.encode())  # Password needs to be bytes
                    print(f"The password is found in line {test} and the password is: {word}")
                    return test  # Return the attempt number once the password is found
                except:
                    continue
    return 0  # Return 0 if no password is found

password_list = input("Enter the location of password list: ")
zip_file = input("Enter the location of a zip file: ").strip("'\"")

# Handle possible errors while opening the zip file
try:
    obj = zipfile.ZipFile(zip_file)
except Exception as e:
    print(f"Error opening zip file: {e}")
    exit()

# Now we count attempts while the program is checking passwords
attempts = crack_password(password_list, obj)

if attempts == 0:
    print("The password isn't in the list.")
else:
    print(f"There were {attempts} attempts to guess the password.")


# /Volumes/Storage/Github/Python/Python/training/some_small_projects/cracking_zip_file_password/password.txt
# /Volumes/Storage/Github/Python/Python/training/some_small_projects/cracking_zip_file_password/protected.zip

