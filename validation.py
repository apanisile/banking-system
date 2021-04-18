
def account_number_validation(account_number):
    if account_number:
        try:
            if len(str(account_number)) == 10:
                return True

        except ValueError:
            print("Account Number has to be integers")
            return False

    else:
        print("Account Number is a required field")


