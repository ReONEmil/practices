"""


Password Checker: Create a program that prompts the user to enter a password. If the
password contains less than 8 characters, prompt the user to enter a new password until the
password meets the criteria. Use a while loop with continue to skip to the next iteration if the
password length is sucient.


"""

while True:
    password = input("Enter your password: ").strip()

    password_witoutspaces = password.replace(" ", "")

    if len(password_witoutspaces) < 8:
        print("Your password is too short, must be at least 8 characters long")
        continue

    print("Password accepted")
    break
