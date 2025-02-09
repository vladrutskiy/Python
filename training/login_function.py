# trying to check login and passwords from dictionary

# importing a dictionary
from usernames_passwords import login_password_list 

# checking if the entered credentials match any in the dictionary
def check_credentials(user_name, user_pass):
   
    for log_pair, pass_pair in login_password_list.login_password_list1.items():  
        if log_pair == user_name and pass_pair == user_pass:
            return True
    return False

# Login attempt counter
attempt1 = 0
attempt2 = 5  

def login2():
    # Get user input
    user_name = input("Please enter user name: \n").lower()
    user_pass = input("Please enter password: \n").lower()

    # Check if credentials are valid
    if check_credentials(user_name, user_pass):
        print(f"Login is successful, welcome {user_name.upper()}")
        return True
    return False

#  loop for login attempts
while True:
    if login2():
        break  
    attempt1 += 1
    if attempt1 >= attempt2:
        print("Login failed. Too many attempts.")
        break  
    
    print("Incorrect username or password. Please try again.")

