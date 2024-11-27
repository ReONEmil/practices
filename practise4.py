"""

User Authentication System: Create a simple user authentication system where the user has
three attempts to enter the correct username and password. If the user fails three times,
display a message and terminate the program. Use a while loop with a counter and break to
limit the number of attempts.

"""


correct_username = input("Set your username: ")

while len(correct_username) < 4 or " " in correct_username:
    print("Username must contain at least 4 characters.")
    correct_username = input("Set your username: ")


correct_password = input("Set your password: ")

while len(correct_password) < 8 or " " in correct_password:
    print("Password must contatin at least 8 characters.")
    correct_password = input("Set your password: ")


attempts = 0
max_attempts = 3

while attempts < max_attempts:
    username = input("Enter username: ")
    password = input("Enter password: ")


    if len(username) < 4:
        print("Username must contain at least 4 characters.")
        attempts += 1
        continue

    if len(password) < 8:
        print("Password must contain at least 8 characters.")
        attempts += 1
        continue

    if username == correct_username and password == correct_password:
        print("Login succesfull.")
        break
    else:
        attempts += 1
        print(f"Incorrect username or password. You have {max_attempts - attempts} attempts left")

if attempts == max_attempts:
    print("Too many attempts. Your access denied")

