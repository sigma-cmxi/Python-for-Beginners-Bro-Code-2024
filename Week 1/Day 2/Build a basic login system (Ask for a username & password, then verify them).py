username = input("Enter your username: ").strip().lower()
password = input("Enter your password: ").strip()

correct_username = "admin"
correct_password = "1234"

if username == correct_username and password == correct_password:
    print("You are admin")
else:
    if username != correct_username:
        print("Incorrect username")
    else:
        print("Incorrect password")