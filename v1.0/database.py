import os
import loading
import validation

db_path = "data/user_record/"


def create(account_from_user, first_name, last_name, email, password):
    print("Creating new user data")
    print("========================================")
    completion_state = False
    user_details = first_name + "," + last_name + "," + email + "," + password
    if does_account_number_exist(account_from_user):
        return False

    if does_email_exist(email):
        print("User already exists")
        return False

    try:
        f = open(db_path + str(account_from_user) + ".txt", "x")

    except FileExistsError:
        does_file_contain_data = read(db_path + str(account_from_user) + ".txt")
        if not does_file_contain_data:
            delete(account_from_user)

    else:
        f.write(str(user_details))
        completion_state = True
    finally:
        f.close();
        return completion_state


def does_email_exist(email):
    print("Checking if email exists...")
    loading.checking()
    all_users = os.listdir(db_path)

    for user in all_users:
        user_list = str.split(read(user), ',')
        if email in user_list:
            return True
    return False


def does_account_number_exist(account_number):
    print("Checking if account number exists...")
    loading.checking()
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


def read(account_from_user):
    print("Reading user data")
    print("========================================")
    is_account_number_valid = validation.account_number_validation(account_from_user)
    try:
        if is_account_number_valid:
            # Open a file
            f = open(db_path + str(account_from_user) + ".txt", "r")
        else:
            f = open(db_path + account_from_user, "r")
    except FileNotFoundError:
        print("User Not Found")
    except FileExistsError:
        print("User already exists")
    except TypeError:
        print("Invalid account format")
    else:
        return f.readline()
    return False


def authenticated_user(account_number, password):
    if does_account_number_exist(account_number):
        user = str.split(read(account_number), ',')
        if password == user[3]:
            return user

    return False


loading.start()