
def account_number_validation(account_from_user):
    if account_from_user:
        try:
            int(account_from_user)
            if len(str(account_from_user)) == 10:
                return True
            else:
                print("Account Number cannot be less or more than 10")
            return False
        except ValueError:
            print("Account Number has to be integers")
            return False

    else:
        print("Account Number is a required field")
