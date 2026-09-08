import json
import random
import string

MASTER_PASSWORD = "1234"

try:
    with open("passwords.json", "r") as file:
        passwords = json.load(file)
except FileNotFoundError:
    passwords = []


print("===== PASSWORD MANAGER =====")

master_password = input("Enter master password: ")

if master_password != MASTER_PASSWORD:
    print("Incorrect master password!")
else:
    print("Access granted!")

    while True:
        print("\n===== PASSWORD MANAGER =====")
        print("1. Add Password")
        print("2. View Passwords")
        print("3. Search Password")
        print("4. Delete Password")
        print("5. Generate Password")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            website = input("Enter website/app name: ")
            username = input("Enter username: ")
            password = input("Enter password: ")

            account = {
                "website": website,
                "username": username,
                "password": password
            }

            passwords.append(account)

            with open("passwords.json", "w") as file:
                json.dump(passwords, file, indent=4)

            print("Password added successfully!")

        elif choice == "2":
            print("\n===== SAVED PASSWORDS =====")

            if len(passwords) == 0:
                print("No passwords saved!")
            else:
                show_passwords = input("Show passwords? (y/n): ")

                for i, account in enumerate(passwords, start=1):
                    if show_passwords.lower() == "y":
                        password = account["password"]
                    else:
                        password = "****"

                    print(
                        i,
                        ".",
                        account["website"],
                        "-",
                        account["username"],
                        "-",
                        password
                    )

        elif choice == "3":
            search = input("Enter website/app name to search: ")

            found = False

            for account in passwords:
                if account["website"].lower() == search.lower():
                    print("\nWebsite:", account["website"])
                    print("Username:", account["username"])
                    print("Password:", account["password"])
                    found = True

            if not found:
                print("Password not found!")

        elif choice == "4":
            print("\n===== DELETE PASSWORD =====")

            if len(passwords) == 0:
                print("No passwords saved!")
            else:
                for i, account in enumerate(passwords, start=1):
                    print(i, ".", account["website"], "-", account["username"])

                try:
                    number = int(input("Enter password number to delete: "))

                    if number < 1 or number > len(passwords):
                        print("Invalid password number!")
                    else:
                        deleted = passwords.pop(number - 1)

                        with open("passwords.json", "w") as file:
                            json.dump(passwords, file, indent=4)

                        print("Password deleted:", deleted["website"])

                except ValueError:
                    print("Please enter a valid number!")

        elif choice == "5":
            print("\n===== PASSWORD GENERATOR =====")

            try:
                length = int(input("Enter password length: "))

                if length < 4:
                    print("Password length should be at least 4!")
                else:
                    characters = (
                        string.ascii_letters
                        + string.digits
                        + string.punctuation
                    )

                    generated_password = ""

                    for i in range(length):
                        generated_password += random.choice(characters)

                    print("Generated Password:", generated_password)

            except ValueError:
                print("Please enter a valid number!")

        elif choice == "6":
            print("Thank you for using Password Manager!")
            break

        else:
            print("Invalid choice!")