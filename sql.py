import mysql.connector

database = "banking_system"


def init():
    mydb = mysql.connector.connect(host="localhost", user="lala", password="Apanisile123*")
    mycursor = mydb.cursor()
    try:
        mycursor.execute(f"CREATE DATABASE {database}")
        check_table()
    except:
        check_table()


def check_table():
    mydb = mysql.connector.connect(host="localhost", user="lala", password="Apanisile123*", database=database)
    mycursor = mydb.cursor()
    try:
        mycursor.execute(
            "CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, account_number INT(10), first_name CHAR("
            "50), last_name CHAR(50), email varchar(50), password char(50), balance int(50))")
    except:
        return True


def insert_details(account_number, first_name, last_name, email, password, balance):
    mydb = mysql.connector.connect(host="localhost", user="lala", password="Apanisile123*", database=database)
    mycursor = mydb.cursor()

    sql = "INSERT INTO users (account_number, first_name, last_name, email, password, balance) VALUES (%s, %s, %s, " \
          "%s, %s, %s) "
    val = (f"{account_number}", f"{first_name}", f"{last_name}", f"{email}", f"{password}", f"{balance}")
    mycursor.execute(sql, val)
    mydb.commit()
    print("User registered.")
    return True


def locate_account(account_number):
    mydb = mysql.connector.connect(host="localhost", user="lala", password="Apanisile123*", database=database)
    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT account_number FROM users WHERE account_number = '{account_number}'")
    result = mycursor.fetchone()
    try:
        if account_number == result[0]:
            return True
        else:
            return False
    except TypeError:
        print("Account number not registered")


def locate_account_password(account_number, password):
    mydb = mysql.connector.connect(host="localhost", user="lala", password="Apanisile123*", database=database)
    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT password FROM users WHERE account_number = '{account_number}'")
    result = mycursor.fetchone()
    if password == result[0]:
        return True
    else:
        return False


# locate_account_password(404491587, 1234)


def user_name(account_number):
    mydb = mysql.connector.connect(host="localhost", user="lala", password="Apanisile123*", database=database)
    mycursor = mydb.cursor()

    mycursor.execute(f"SELECT first_name FROM users WHERE account_number = '{account_number}'")
    result = mycursor.fetchone()
    return result[0]


def get_balance(account_number):
    mydb = mysql.connector.connect(host="localhost", user="lala", password="Apanisile123*", database=database)
    mycursor = mydb.cursor()

    mycursor.execute(f"SELECT balance FROM users WHERE account_number = '{account_number}'")
    result = mycursor.fetchone()
    return int(result[0])


def update_balance(account_number, new_balance):
    mydb = mysql.connector.connect(host="localhost", user="lala", password="Apanisile123*", database=database)
    mycursor = mydb.cursor()

    sql = "UPDATE users SET balance = %s WHERE account_number = %s"
    val = (f"{new_balance}", f"{account_number}")
    mycursor.execute(sql, val)
    mydb.commit()
    print("Done")


class update():

    def update_fname(account_number, first_name):
        mydb = mysql.connector.connect(host="localhost", user="lala", password="Apanisile123*", database=database)
        mycursor = mydb.cursor()

        sql = "UPDATE users SET first_name = %s WHERE account_number = %s"
        val = (f"{first_name}", f"{account_number}")
        mycursor.execute(sql, val)
        mydb.commit()
        print("First name Updated")

    def update_lname(account_number, last_name):
        mydb = mysql.connector.connect(host="localhost", user="lala", password="Apanisile123*", database=database)
        mycursor = mydb.cursor()

        sql = "UPDATE users SET last_name = %s WHERE account_number = %s"
        val = (f"{last_name}", f"{account_number}")
        mycursor.execute(sql, val)
        mydb.commit()
        print("First name Updated")

    def update_email(account_number, email):
        mydb = mysql.connector.connect(host="localhost", user="lala", password="Apanisile123*", database=database)
        mycursor = mydb.cursor()

        sql = "UPDATE users SET email = %s WHERE account_number = %s"
        val = (f"{email}", f"{account_number}")
        mycursor.execute(sql, val)
        mydb.commit()
        print("First name Updated")


init()
