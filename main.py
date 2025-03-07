import getpass

# Sample database
users = {}

# Sign-up function
def sign_up():
    username = input("Enter a username: ")
    if username in users:
        print("Username already exists. Try logging in.")
        return
    password = getpass.getpass("Enter a password: ")
    users[username] = {"password": password, "balance": 0}
    print("Account created successfully!")

# Login function
def login():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")

    if username in users and users[username]["password"] == password:
        print(f"Welcome, {username}!")
        return username
    else:
        print("Invalid username or password.")
        return None

# Withdraw function
def withdraw(username):
    amount = float(input("Enter amount to withdraw: "))
    if amount > users[username]["balance"]:
        print("Insufficient balance.")
    else:
        users[username]["balance"] -= amount
        print(f"Withdrawal successful. New balance: {users[username]['balance']}")

# Deposit function
def deposit(username):
    amount = float(input("Enter amount to deposit: "))
    users[username]["balance"] += amount
    print(f"Deposit successful. New balance: {users[username]['balance']}")

# Balance details function
def balance_details(username):
    print(f"Your current balance is: {users[username]['balance']}")

# Main program loop
while True:
    print("\nWelcome to the ATM System")
    print("1. Sign Up")
    print("2. Login")
    print("3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        sign_up()
    elif choice == "2":
        user = login()
        if user:
            while True:
                print("\n1. Withdraw")
                print("2. Deposit")
                print("3. Balance Details")
                print("4. Logout")
                action = input("Choose an option: ")

                if action == "1":
                    withdraw(user)
                elif action == "2":
                    deposit(user)
                elif action == "3":
                    balance_details(user)
                elif action == "4":
                    print("Logging out...")
                    break
                else:
                    print("Invalid choice, please try again.")
    elif choice == "3":
        print("Exiting... Have a nice day!")
        break
    else:
        print("Invalid option, please try again.")
