class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount!")
        else:
            self.__balance += amount
            print("Money deposited successfully!")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount!")
        elif amount > self.__balance:
            print("Insufficient balance!")
        else:
            self.__balance -= amount
            print("Money withdrawn successfully!")
    def check_balance(self):
        print("Account Holder:", self.name)
        print("Current Balance:", self.__balance)
account = BankAccount("Tharnika", 5000)
while True:
    print("\n--- BANK ACCOUNT ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    try:
        if choice == "1":
            amount = float(input("Enter amount: "))
            account.deposit(amount)

        elif choice == "2":
            amount = float(input("Enter amount: "))
            account.withdraw(amount)

        elif choice == "3":
            account.check_balance()
        elif choice == "4":
            print("Thank you!")
            break
        else:
            print("Invalid choice!")
    except ValueError:
        print("Please enter a valid number!")
