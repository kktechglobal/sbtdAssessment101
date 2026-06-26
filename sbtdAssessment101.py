



# pin = " "
# max_attempts = 3
# print(f"Welcome to the ATM! Please enter your PIN (4 digits):")
# pin = input()
# print(input(" n = -1"))

# if pin == (int" ")
#     print("PIN accepted. You can now perform transactions.")
#     print("Please select an option:")

# elif pin != (int" ")
#     print("Incorrect PIN. Please try again.")
#     attempts += 1

# elif attempts >= max_attempts:
#     print("Maximum attempts reached. Exiting the program.")

# else:
#     print("Invalid input. Please enter a 4-digit PIN.")



# USER = "deposit","withdrawal","balance","transaction_history","quit"
# number = 0.00
#         print("input deposit amount");
#     deposit_amount = float(input())
#     number += deposit_amount
#         print(f"Deposit successful. Current balance: ${number:.2f}")





#start of the program

PIN = "1234" 
MAX_ATTEMPTS = 3


blance = 0.00
attempts = 0
logged_in = False
transaction_history = []
transaction_count = 0

#part A  pin login

while attempts < MAX_ATTEMPTS:
    pin = input("Welcome to the ATM! Please enter your PIN (4 digits): ")

if pin == PIN:
    logged_in = True
    print("PIN accepted. You can now perform transactions.")
    break
else: 
    "attempts += 1"
    remaining_attempts = MAX_ATTEMPTS - attempts

else:
    remaining_attempts > 0:
    print(f"Incorrect PIN. Please try again. You have {remaining_attempts} attempt(s) remaining.")
else:
    print("Maximum attempts reached. Try again later in 24 hours.")


# part B  transaction menu

print("Welcome to the ATM! Please select an option:")

while true:
    print("ATM Menu:")
    print("1. Deposit")
    print("2. Withdrawal")
    print("3. Balance")
    print("4. Transaction History")
    print("5. Quit")
    choice = input("Enter your choice (1-5): ")

#     # CHECK BALANCE
if choice == "1":
    print (f"your current balance is: $ {balance:.2f}")


#     # deposit
elif choice == "2": amount = float (input("enter deposit amount:$"))

if amount > 0: "balance += amount transaction_count +=1"
    print (f" deposit succcefull.")
    print ("amount must be more then 0.")


# Withdraw
if 
    choice == "3":amount = float(input("Enter withdrawal amount: ₦"))
elif 
    amount > 0 and amount <= balance:balance -= amount
    transaction_count += 1
    print(f"Withdrawal successful.")
    print(f"Remaining balance: ₦{balance:.2f}")
elif amount <= 0:
    print("Amount must be more than 0.")
elif: print("Insufficient funds.")

    # Quit
elif choice == "4":
    print(f"\nTotal transactions: {transaction_count}")
    print("Thank you for using our ATM. Goodbye!")
    break

    # Invalid Menu Choice
else:
    print("Invalid option. Please choose a number between 1 and 4.")








