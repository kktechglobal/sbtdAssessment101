



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


balance = 0.00
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
        while True:
            print("ATM Menu:")
            print("1. Balance")
            print("2. Deposit")
            print("3. Withdrawal")
            print("4. Quit")
            choice = input("Enter your choice (1-4): ")
            if choice == "1":
                print (f"your current balance is: {balance}")

            # deposit
            elif choice == "2": 
                amount = float (input("enter deposit amount:$"))
                if amount >= 0: 
                    balance = balance + amount
                    print (f" deposit succcefull.")
                else:
                    print ("amount must be more then 0.")

            # Withdraw
            elif choice == "3":
                amount = float(input("Enter withdrawal amount: ₦"))
                if amount > 0 and amount <= balance:
                    balance -= amount
                    transaction_count += 1
                    print(f"Withdrawal successful.")
                    print(f"Remaining balance: ₦{balance:.2f}")
                else:
                    print("Invalid withdrawal amount or insufficient funds.")

            # Quit
            elif choice == "4":
                print(f"\nTotal transactions: {transaction_count}")
                print("Thank you for using our ATM. Goodbye!")
                exit()
    else:
        attempts = attempts + 1
        print("Incorrect PIN. Please try again.")
        if attempts == MAX_ATTEMPTS:
            print("Maximum attempts reached. Exiting the program.......")
            exit()


































    # else: 
    #     attempts += 1
    #     if attempts == 3:
    #         print("Maximum attempts reached. Exiting the program.")
        
    # while True:
    #     print("ATM Menu:")
    #     print("1. Deposit")
    #     print("2. Withdrawal")
    #     print("3. Balance")
    #     print("4. Transaction History")
    #     print("5. Quit")
    #     choice = input("Enter your choice (1-5): ")

# #     # CHECK BALANCE
# if choice == "1":
#     print (f"your current balance is: $ {balance:.2f}")


# #     # deposit
# elif choice == "2": amount = float (input("enter deposit amount:$"))

# if amount > 0: "balance += amount transaction_count +=1"
#     print (f" deposit succcefull.")
#     print ("amount must be more then 0.")


# # Withdraw
# if 
#     choice == "3":amount = float(input("Enter withdrawal amount: ₦"))
# elif 
#     amount > 0 and amount <= balance:balance -= amount
#     transaction_count += 1
#     print(f"Withdrawal successful.")
#     print(f"Remaining balance: ₦{balance:.2f}")
# elif amount <= 0:
#     print("Amount must be more than 0.")
# elif: print("Insufficient funds.")

#     # Quit
# elif choice == "4":
#     print(f"\nTotal transactions: {transaction_count}")
#     print("Thank you for using our ATM. Goodbye!")
#     break

#     # Invalid Menu Choice
# else:
#     print("Invalid option. Please choose a number between 1 and 4.")








