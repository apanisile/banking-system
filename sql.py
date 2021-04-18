import mysql.connector
import account

"""def create_database():
    db = pymysql.connect("localhost", "lala", "Apanisile123*", "python_test")
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    # execute SQL query using execute() method.
    cursor.execute("SELECT VERSION()")
    # Fetch a single row using fetchone() method.
    data = cursor.fetchone()
    print("Database version : %s " % data)
    # disconnect from server
    db.close()


create_database()
"""

database = "banking_system"


def init():
    mydb = mysql.connector.connect(host="localhost", user="lala", password="Apanisile123*")
    mycursor = mydb.cursor()
    try:
        mycursor.execute(f"CREATE DATABASE {database}")
        print("Database Created")
    except:
        print("Database exists")
        check_table()


def check_table():
    mydb = mysql.connector.connect(host="localhost", user="lala", password="Apanisile123*", database=database)
    mycursor = mydb.cursor()
    try:
        mycursor.execute(
            "CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, account_number INT(10), first_name CHAR("
            "50), last_name CHAR(50), email varchar(50), password char(50))")
    except:
        # mycursor.execute("ALTER TABLE users ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
        return True
    # check_table_exist()


def connect():
    mydb = mysql.connector.connect(host="localhost", user="lala", password="Apanisile123*", database=database)
    mycursor = mydb.cursor()


def insert_details(account_number, first_name, last_name, email, password):
    mydb = mysql.connector.connect(host="localhost", user="lala", password="Apanisile123*", database=database)
    mycursor = mydb.cursor()

    sql = "INSERT INTO users (account_number, first_name, last_name, email, password) VALUES (%s, %s, %s, %s, %s)"
    val = (f"{account_number}", f"{first_name}", f"{last_name}", f"{email}", f"{password}")
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
    return True


def locate_account(account_number):
    mydb = mysql.connector.connect(host="localhost", user="lala", password="Apanisile123*", database=database)
    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT account_number FROM users WHERE account_number = '{account_number}'")
    result = mycursor.fetchone()
    int(result[0])
    if account_number == result[0]:
        return True
    else:
        print("Not found")
        return False


def locate_account_password(account_number, password):
    mydb = mysql.connector.connect(host="localhost", user="lala", password="Apanisile123*", database=database)
    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT password FROM users WHERE account_number = '{account_number}'")
    result = mycursor.fetchone()
    if password == result[0]:
        return True
    else:
        return False


#locate_account_password(404491587, 1234)


def user_name(account_number):
    mydb = mysql.connector.connect(host="localhost", user="lala", password="Apanisile123*", database=database)
    mycursor = mydb.cursor()

    mycursor.execute(f"SELECT first_name FROM users WHERE account_number = '{account_number}'")
    result = mycursor.fetchone()
    return result[0]


#user_name(404491587)
