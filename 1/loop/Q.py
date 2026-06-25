def atm():
    accounts = {
        "ram": 400,
        "hari": 400,
        "sita": 800
    }

    def withdraw():
        user = input("Enter username: ")
        amount = int(input("Enter amount to withdraw: "))
        if user not in accounts:
            print("User not found")
            return
        if amount > accounts[user]:
            print("Insufficient Balance")
            return
        accounts[user] -= amount
    while True:
        withdraw()
        if input("Continue? (y/n): ") != "y":
            break
    withdraw()
atm()

def account(balance):
    current_balance=balance
    def with_draw(amount):
        nonlocal balance
        if balance >= amount:
            balance= balance-amount:
            return f" "
        else:
            return " "
user_ram=account(500)
print(user_ram.__closure__[0].cell_contents)