import os

db_path = "data/user_record/"


def create(account_number, user_details):
    print("Creating new user data")
    completion_state = False
    if does_account_number_exist(account_number):
        return False

    try:
        f = open(db_path + str(account_number) + ".txt", "x")

    except FileExistsError:
        print("User already exists")
        delete(account_number)

    else:
        f.write(str(user_details))
        completion_state = True
    finally:
        f.close()
    return completion_state


def does_email_exist(email):
    print("Locating user email")
    all_users = os.listdir(db_path)
    for user in all_users:
        user_list = str.split(read(user), ',')
        if email in user_list:
            return True
    return False


def does_account_number_exist(account_number):
    print("Locating user account")
    all_users = os.listdir(db_path)
    for user in all_users:
        if user == str(account_number) + ".txt":
            return True
    return False


def update(user_account_number):
    print("Update user data")


def delete(account_number):
    print("User record deleted")
    is_deleted_successful = False
    if os.path.exists(db_path + str(account_number) + ".txt"):
        try:
            os.remove(db_path + str(account_number) + ".txt")
            is_deleted_successful = True

        except FileNotFoundError:
            print("User Not found")
        finally:
            return is_deleted_successful


def read(account_number):
    print("Reading user data")
    try:
        # Open a file
        f = open(db_path + str(account_number) + ".txt", "r+")
    except FileNotFoundError:
        print("User Not Found")
    else:
        return f.readline()
    return False


def authenticated_user(account_number, password):
    if does_account_number_exist(account_number):
        user = str.split(read(account_number), ',')
        if password == user[3]:
            return user

    return False
