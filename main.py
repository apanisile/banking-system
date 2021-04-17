import account as ac

database = {}




def init():
    print("Do you have an account with us? 1 (Yes) 2 (No)")
    answerRequest = int(input("> "))
    if (answerRequest == 1):
        haveAccount = True
        login()
    elif (answerRequest == 2):
        haveAccount = True
        register()
    else:
        print("You dont have an account!")


def register():
    fname = input("Please enter your first name: \n")
    lname = input("Enter your last name: \n")
    email = input("Enter your email: \n")
    password = input("Enter your pasword: \n")

    account_no = ac.generating_account()

    print(account_no)

    database[account_no] = [fname, lname, email, password]
    print(f"{fname}{lname} your account has been successful created!")
    print("You can now login")
    login(account_no)


def login(account_no):
    print("=======================================")
    print("Registration Successful")
    print("========================================")
    print(f"Your account number is : {account_no}")
    accountFromUser = int(input("Enter your account number"))
    if accountFromUser != account_no:
        print("Sorry! No account found")


######## ACTUAL BANKING #######
init()
