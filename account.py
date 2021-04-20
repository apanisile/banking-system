import random


def generating_account():
    account_number = random.randrange(111111111, 9999999999)
    return account_number


def generating_account_db():
    account_number = random.randrange(111111111, 999999999)
    return account_number
