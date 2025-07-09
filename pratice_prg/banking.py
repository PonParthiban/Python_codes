#banking program
balance = 0
is_running = True
#Functions to perform baking operations
def show_balance():
     print(f"The balance is :{balance}")
def withdraw(): 
    global balance
    amount = int(input("Enter the amount to be withdrawn: "))
    if amount > balance:
         print("Insufficent balance,try again")
    else:
         balance -= amount
         print(f"The {amount} is withdrawn sucessfully")
def deposit():
     global balance
     amount = int(input("Enter the amount to be deposited: "))
     balance += amount
     print(f"The {amount} is sucessfully deposited ")

while is_running:
    print("******************************************************************")
    print("\nBanking Program")
    print("******************************************************************")
    print("1.Show Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")
    choice = int(input("Enter the choice(1/2/3/4): "))
    match choice:
            case 1:
                 show_balance()
            case 2:
                 deposit()           
            case 3:
                 withdraw()
            case 4:
                 is_running = False
                 print("Thankyou for using the banking program <3")
                 print("Exiting......")
            case _:
                 print("Invalid choice,try again!!")
    
