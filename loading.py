import time
import sys


def start():
    t = 0
    while t < 4:
        sys.stdout.write('\rStarting |')
        time.sleep(0.2)
        sys.stdout.write('\rStarting /')
        time.sleep(0.2)
        sys.stdout.write('\rStarting -')
        time.sleep(0.2)
        sys.stdout.write('\rStarting \\')
        time.sleep(0.2)
        t += 1
    sys.stdout.write('\r \n')


def load():
    t = 0
    while t < 4:
        sys.stdout.write('\rloading |')
        time.sleep(0.2)
        sys.stdout.write('\rloading /')
        time.sleep(0.2)
        sys.stdout.write('\rloading -')
        time.sleep(0.2)
        sys.stdout.write('\rloading \\')
        time.sleep(0.2)
        t += 1
    sys.stdout.write('\rDone!   \n')


def checking():
    t = 0
    while t < 4:
        sys.stdout.write('\rChecking |')
        time.sleep(0.2)
        sys.stdout.write('\rChecking /')
        time.sleep(0.2)
        sys.stdout.write('\rChecking -')
        time.sleep(0.2)
        sys.stdout.write('\rChecking \\')
        time.sleep(0.2)
        t += 1
    sys.stdout.write('\rDone!   \n')
