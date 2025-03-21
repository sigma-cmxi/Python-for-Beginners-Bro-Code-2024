username = input("Enter your username: ").strip()
if (
    len(username) > 12
    or not username.isalpha()
    or " " in username
):
    print("invalid username")
else:
    print(f"welcome {username}")
