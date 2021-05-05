import loading
import sql


def deposit(account_from_user):
    amount_to_deposit = int(input("How much would you like to deposit: \n >"))
    balance = sql.get_balance(account_from_user)
    new_balance = amount_to_deposit + balance
    sql.update_balance(account_from_user, new_balance)
    print(f"Your new balance is: {new_balance}")
    print("Deposited...")


def withdraw(account_from_user):
    amount_to_withdraw = int(input("How much would you like to withdraw: \n >"))
    balance = sql.get_balance(account_from_user)
    if balance >= amount_to_withdraw:
        new_balance = balance - amount_to_withdraw
        print(f"Your new balance is: {new_balance}")
        sql.update_balance(account_from_user, new_balance)
    else:
        print("Insufficient Balance")


def loan():
    print("Loan")


def update_profile(account_from_user):
    print("What would you like to edit:")
    print("> 1. First Name")
    print("> 2. Last Name")
    print("> 3. Email")
    print("> 4. Delete Account")
    option = int(input("> "))
    loading.load()
    if option == 1:
        first_name = input("What would you like to change your first name to?")
        sql.update.update_fname(account_from_user, first_name)
        print(f"Your new First name is : {first_name}")
    elif option == 2:
        last_name = input("What would you like to change your last name to?")
        sql.update.update_fname(account_from_user, last_name)
        print(f"Your new last name is : {last_name}")
    elif option == 3:
        email = input("What would you like to change your email to?")
        sql.update.update_fname(account_from_user, email)
        print(f"Your new First name is : {email}")
    elif option == 4:
        loading.load()
        sql.delete_user(account_from_user)
    else:
        print("Invalid option")
        update_profile(account_from_user)
