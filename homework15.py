
def username_check(username):
    if len(username) > 3:
        print("Valid username")
    else:
        print("Invalid username")


def password_check(password):
    if len(password) >= 8 and any(char.isdigit() for char in password):
        print("Valid password")
    else:
        print("Invalid password")


def email_check(email):
    if "@" in email:
        print("Valid email")
    else:
        print("Invalid email")


username = input("Enter username: ")
password = input("Enter password: ")
email = input("Enter email: ")

username_check(username)
password_check(password)
email_check(email)
