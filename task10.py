import re

def validate_password(password):
   
    if (re.search(r"[a-z]", password) and
        re.search(r"[A-Z]", password) and
        re.search(r"[0-9]", password) and
        re.search(r"[$#@]", password) and
        6 <= len(password) <= 16):
        return True
    else:
        return False


password = input("Enter your password: ")
if validate_password(password):
    print("Password is valid.")
else:
    print("Password is not valid.")


