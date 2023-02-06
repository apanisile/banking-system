import mysql.connector
import psycopg2
import loading
import main2

database = "banking_system"


def init():
    # mydb = psycopg2.connect(host="localhost", user="ifeoluwa", password="ifeoluwa")
    mydb = psycopg2.connect(database="bankin_system", host="localhost", user="ifeoluwa", password="ifeoluwa")
    mycursor = mydb.cursor()
    try:
        check_table()
    except:
        check_table()
        mycursor.execute(f"CREATE DATABASE {database}")

def check_table():
    # mydb = mysql.connector.connect(host="localhost", user="lala", password="Apanisile123*", database=database)
    mydb = psycopg2.connect(database="bankin_system",
                            host="localhost", user="ifeoluwa", password="ifeoluwa")
    mycursor = mydb.cursor()
    try:
        return True
    except:
        mycursor.execute(
            "CREATE TABLE users (id SERIAL PRIMARY KEY, account_number INT, first_name VARCHAR, last_name VARCHAR, email varchar, password varchar, balance int)")

def insert_details(account_number, first_name, last_name, email, password, balance):
    # mydb = mysql.connector.connect(host="localhost", user="lala", password="Apanisile123*", database=database)
    mydb = psycopg2.connect(database="bankin_system",
                            host="localhost", user="ifeoluwa", password="ifeoluwa")
    mycursor = mydb.cursor()

    sql = "INSERT INTO users (account_number, first_name, last_name, email, password, balance) VALUES (%s, %s, %s, " \
          "%s, %s, %s) "
    val = (f"{account_number}", f"{first_name}", f"{last_name}", f"{email}", f"{password}", f"{balance}")
    mycursor.execute(sql, val)
    mydb.commit()
    print("User registered.")
    return True

def locate_account(account_number):
    # mydb = mysql.connector.connect(host="localhost", user="lala", password="Apanisile123*", database=database)
    mydb = psycopg2.connect(database="bankin_system",
                            host="localhost", user="ifeoluwa", password="ifeoluwa")
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
    # mydb = mysql.connector.connect(host="localhost", user="lala", password="Apanisile123*", database=database)
    mydb = psycopg2.connect(database="bankin_system",
                            host="localhost", user="ifeoluwa", password="ifeoluwa")
    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT password FROM users WHERE account_number = '{account_number}'")
    result = mycursor.fetchone()[0]
    if password == result:
        return True
    else:
        return False


def user_name(account_number):
    # mydb = mysql.connector.connect(host="localhost", user="lala", password="Apanisile123*", database=database)
    mydb = psycopg2.connect(database="bankin_system",
                            host="localhost", user="ifeoluwa", password="ifeoluwa")
    mycursor = mydb.cursor()

    mycursor.execute(f"SELECT first_name FROM users WHERE account_number = '{account_number}'")
    result = mycursor.fetchone()
    return result[0]


def get_balance(account_number):
    # mydb = mysql.connector.connect(host="localhost", user="lala", password="Apanisile123*", database=database)
    mydb = psycopg2.connect(database="bankin_system",
                            host="localhost", user="ifeoluwa", password="ifeoluwa")
    mycursor = mydb.cursor()

    mycursor.execute(f"SELECT balance FROM users WHERE account_number = '{account_number}'")
    result = mycursor.fetchone()
    return int(result[0])


def update_balance(account_number, new_balance):
    # mydb = mysql.connector.connect(host="localhost", user="lala", password="Apanisile123*", database=database)
    mydb = psycopg2.connect(database="bankin_system",
                            host="localhost", user="ifeoluwa", password="ifeoluwa")
    mycursor = mydb.cursor()

    sql = "UPDATE users SET balance = %s WHERE account_number = %s"
    val = (f"{new_balance}", f"{account_number}")
    mycursor.execute(sql, val)
    mydb.commit()
    print("Done")


def delete_user(account_number):
    #mydb = mysql.connector.connect(host="localhost", user="lala", password="Apanisile123*", database=database)
    mydb = psycopg2.connect(database="bankin_system",
                            host="localhost", user="ifeoluwa", password="ifeoluwa")
    mycursor = mydb.cursor()
    confirm_delete = int(input("Are you sure you want to delete your account? 1 (Yes) 2 (No) \n >"))
    if confirm_delete == 1:
        sql = "DELETE FROM users WHERE account_number = %s"
        print("Account Deleted!")
        loading.load()
        print("Thank you for banking with us!")
        loading.load()
        print("Bye!")
        exit(0)
    elif confirm_delete == 2:
        print("Alright!")
        main2.bank_operations()
    else:
        print("Wrong input! \n Please try again")
        delete_user(account_number)


class update():

    def update_fname(account_number, first_name):
        #mydb = mysql.connector.connect(host="localhost", user="lala", password="Apanisile123*", database=database)
        mydb = psycopg2.connect(database="bankin_system",
                            host="localhost", user="ifeoluwa", password="ifeoluwa")
        mycursor = mydb.cursor()

        sql = "UPDATE users SET first_name = %s WHERE account_number = %s"
        val = (f"{first_name}", f"{account_number}")
        mycursor.execute(sql, val)
        mydb.commit()
        print("First name Updated")

    def update_lname(account_number, last_name):
        #mydb = mysql.connector.connect(host="localhost", user="lala", password="Apanisile123*", database=database)
        mydb = psycopg2.connect(database="bankin_system",
                            host="localhost", user="ifeoluwa", password="ifeoluwa")
        mycursor = mydb.cursor()

        sql = "UPDATE users SET last_name = %s WHERE account_number = %s"
        val = (f"{last_name}", f"{account_number}")
        mycursor.execute(sql, val)
        mydb.commit()
        print("First name Updated")

    def update_email(account_number, email):
        #mydb = mysql.connector.connect(host="localhost", user="lala", password="Apanisile123*", database=database)
        mydb = psycopg2.connect(database="bankin_system",
                            host="localhost", user="ifeoluwa", password="ifeoluwa")
        mycursor = mydb.cursor()

        sql = "UPDATE users SET email = %s WHERE account_number = %s"
        val = (f"{email}", f"{account_number}")
        mycursor.execute(sql, val)
        mydb.commit()
        print("First name Updated")


init()
