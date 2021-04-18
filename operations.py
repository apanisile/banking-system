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


def view_profile():
    print("Profile")

