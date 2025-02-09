# trying to check login and passwords from list
from usernames_passwords import login_password_list

# Created a new login function
correct_user_name = login_password_list.correct_login
correct_password = login_password_list.correct_pass1
attempt1 = 0
attempt2 = 2
def login2 ():
    user_name = input("Please enter user name: \n").lower()
    user_pass = input ("Please enter password: \n").lower()
    
    if user_name == correct_user_name and user_pass == correct_password:
        return True
    return False

while True:
        if login2():
            print("Login is successful, welcome", (correct_user_name).upper())
            break
        attempt1 += 1
        if attempt1 >= attempt2:
            print("Login failed")
            break
          
        print("Enter correct user name of password")