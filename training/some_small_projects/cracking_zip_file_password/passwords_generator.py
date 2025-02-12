import random
import string

# Function to generate random passwords
def generate_random_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

# Function to generate a list of common passwords
def generate_common_passwords():
    common_passwords = [
        "123456", "password", "123456789", "12345", "1234", "qwerty", "abc123",
        "password1", "letmein", "123123", "welcome", "iloveyou", "admin", "password123",
        "123qwe", "sunshine", "qwertyuiop", "superman", "iloveyou123", "princess",
        "qwerty123", "dragon", "1q2w3e4r", "football", "monkey", "123321", "letmein123"
    ]
    return common_passwords

# Write passwords to a file
def generate_password_file(filename="passwords.txt", num_random=50):
    with open(filename, "w") as file:
        # Write common passwords first
        common_passwords = generate_common_passwords()
        for password in common_passwords:
            file.write(password + "\n")
        
        # Write random passwords next
        for _ in range(num_random):
            random_password = generate_random_password()
            file.write(random_password + "\n")
    
    print(f"Password file '{filename}' generated with common and random passwords.")

# Generate password file
generate_password_file("passwords.txt", num_random=5000)
