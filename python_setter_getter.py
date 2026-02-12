# Define a class named BankAccount
class BankAccount:

    # Constructor method
    def __init__(self, owner, balance):
        # Public attribute (can be accessed directly)
        self.owner = owner

        # Private attribute using double underscore
        # This prevents direct access from outside the class
        self.__balance = 0

        # Use setter to initialize balance safely
        self.set_balance(balance)

    # ---------------------------
    # Getter Method
    # ---------------------------

    # Method to safely get the private balance
    def get_balance(self):
        # Return the private balance
        return self.__balance

    # ---------------------------
    # Setter Method
    # ---------------------------

    # Method to safely set balance
    def set_balance(self, amount):
        # Validate that balance cannot be negative
        if amount >= 0:
            # Set the private balance
            self.__balance = amount
        else:
            # Print error if invalid value
            print("Balance cannot be negative.")

    # ---------------------------
    # Deposit Method
    # ---------------------------

    # Method to deposit money
    def deposit(self, amount):
        # Check if deposit amount is positive
        if amount > 0:
            # Add amount to private balance
            self.__balance += amount
            print(f"{amount} deposited successfully.")
        else:
            print("Deposit must be positive.")

    # ---------------------------
    # Withdraw Method
    # ---------------------------

    # Method to withdraw money
    def withdraw(self, amount):
        # Check if amount is valid
        if amount > 0:
            # Check if sufficient balance exists
            if amount <= self.__balance:
                # Deduct amount
                self.__balance -= amount
                print(f"{amount} withdrawn successfully.")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal must be positive.")

    # ---------------------------
    # Display Method
    # ---------------------------

    # Method to display account info
    def display_info(self):
        # Print owner and balance (using getter)
        print(f"Owner: {self.owner}")
        print(f"Balance: {self.get_balance()}")


# ---------------------------
# Create Account Object
# ---------------------------

# Create a BankAccount object
account = BankAccount("Alice", 1000)

# Try accessing private attribute directly (will fail)
# print(account.__balance)  # ❌ This will raise an error

# Correct way using getter
print("Current Balance:", account.get_balance())

# Deposit money
account.deposit(500)

# Withdraw money
account.withdraw(300)

# Display account information
account.display_info()


# Output:

# Current Balance: 1000
# 500 deposited successfully.
# 300 withdrawn successfully.
# Owner: Alice
# Balance: 1200

# Process finished with exit code 0
