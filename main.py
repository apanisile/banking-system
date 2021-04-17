import account as ac

database = {}




def init():
    start = False
    print("Do you have an account with us? 1 (Yes) 2 (No)")
    answerRequest = int(input("> "))
    while start == False :
        if (answerRequest == 1):
            haveAccount = True
            login()
        elif (answerRequest == 2):
            haveAccount = True
            register()
        else:
            print("You dont have an account!")

def register():
    print("=======================================")
    print("********** Register *******************")
    print("========================================")
    fname = input("Please enter your first name: \n")
    lname = input("Enter your last name: \n")
    email = input("Enter your email: \n")
    password = input("Enter your password: \n")

    account_no = ac.generating_account()

    print(account_no)

    database[account_no] = [fname, lname, email, password]
    print("=======================================")
    print("Registration Successful")
    print("========================================")
    print(f"Your account number is : {account_no}")
    print(f"{fname}{lname} your account has been successful created!")
    print("You can now login")
    login(account_no)


def login(account_no):
    print("=======================================")
    print("********** Login *******************")
    print("========================================")
    isLoginSuccessful = False
    while isLoginSuccessful == False:
        accountFromUser = int(input("Enter your account number: \n >"))
        password = input("Enter your saved password: \n >")
        for accountFromUser, userDetails in database.items() :
            if accountFromUser == account_no:
                if userDetails[3] == password:
                    isLoginSuccessful = True
                    print("Welcome! ")
                else:
                    print("Sorry! No account found")

        bankOperations()

def bankOperations():
    print("Welcome")


######## ACTUAL BANKING #######
init()
