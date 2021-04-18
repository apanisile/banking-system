import account
import database
import sql
import validation
import loading


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

    account_number = account.generating_account()

    is_user_created = database.create(account_number, first_name, last_name, email, password)

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
    account_from_user = input("Enter your account number: \n >")

    is_valid_account_number = validation.account_number_validation(account_from_user)

    if is_valid_account_number:
        password = input("Enter your password: \n >")
        loading.load()

        user = database.authenticated_user(account_from_user, password)

        if user:
            print("Welcome %s !" % user[1])
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
init()
