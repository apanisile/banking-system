import account
import loading
import sql


def init():
    print("=======================================================")
    print("********** Apanisile Banking System *******************")
    print("=======================================================")
    print("Do you have an account with us? 1 (Yes) 2 (No)")
    answerable = int(input("> "))
    if answerable == 1:
        login()
    elif answerable == 2:
        register()
    else:
        print("Invalid Response!")
        init()


def register():
    print("=======================================")
    print("********** Register *******************")
    print("========================================")
    first_name = input("Please enter your first name: \n")
    last_name = input("Enter your last name: \n")
    email = input("Enter your email: \n")
    password = input("Enter your password: \n")

    account_number = account.generating_account_db()

    is_user_created = sql.insert_details(account_number, first_name, last_name, email, password)

    if is_user_created:
        loading.load()
        print("=======================================")
        print("Registration Successful")
        print("========================================")
        print(f"Your account number is : {account_number}")
        print(f"{first_name} {last_name}, your account has been successful created!", sep=" ")
        print("You can now login")
        login()
    else:
        print("Something went wrong, please try again!")
        loading.load()
        register()


def login():
    print("=======================================")
    print("********** Login *******************")
    print("========================================")
    account_from_user = int(input("Enter your account number: \n >"))

    is_valid_account_number = sql.locate_account(account_from_user)

    if is_valid_account_number:
        password = input("Enter your password: \n >")
        loading.load()

        user = sql.locate_account_password(account_from_user, password)

        if user:
            print(f"Welcome %s !" % sql.user_name(account_from_user))
            bank_operations(user)
        else:
            print("Wrong account number or password")
            login()
    else:
        init()


def bank_operations(user):
    loading.load()
    print("==========================================================")
    print("********** What would you like to do? *******************")
    print("==========================================================")
    print("> 1. Withdraw")
    print("> 2. Deposit")
    print("> 3. Request a Loan")
    print("> 4. View account profile")
    input("\r ")


# ACTUAL BANKING
sql.init()
init()
