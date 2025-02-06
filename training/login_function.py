# a login like function
attempt = 0
max_attempt = 5
def login (username, password):
    user = input("Please enter username: ").lower()
    passs = input("Please enter the password: ").lower()

    if user == username and passs == password:
        return True
    return False
while True :
    if login("rory", "goal"):
        print("The login is successful!")
        break
    attempt += 1
    if attempt >= max_attempt:
        print("something went wrong")
        break
    print("The user name or password are incorrect \n")

    def start_login():
        login()
        