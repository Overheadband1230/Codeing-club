import csv
import subprocess


def option():
    choice = input("Enter C or type 'checkout' to make purchases. If you would like to reset your password press R or "
                   "type 'reset' to reset your password: ")

    if choice.lower() == "c" or choice.lower() == "checkout":
        subprocess.run(["python", "checkout.py"])
        pass

    elif choice.lower() == "reset" or choice.lower() == "r":
        resetPassword()

    elif choice.lower() == "add" or choice.lower() == "add item" or choice.lower() == "a":
        subprocess.run(["python", "foodbank.py"])

    else:
        print("Not a valid option")
        option()


print("Login?")


def resetPassword():
    with open("password.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            oldPass = row[0]

    isValid = False
    while isValid == False:
        newPass = input("Type your new password: ")
        confirm = input("Confirm your new password: ")
        if newPass != confirm and oldPass != password:
            print("Passwords do not match.")
            continue
        elif strengthChecker(newPass) == "Invalid":
            continue
        else:
            isValid = True
            password = newPass
            with open("password.csv", "w", newline='') as file:
                writer = csv.writer(file)
                writer.writerow([password])
        print("Password has been successfully changed!")
    passwordCheck()


def strengthChecker(password):
    # Check for numbers
    containsNum = False
    for character in password:
        if character.isdigit():
            containsNum = True
    if containsNum == False:
        print("Your password needs to have at least one number.")

    # Check length
    if len(password) < 4:
        print("Your password is too short.")
    if len(password) > 8:
        print("Your password is too long.")

    if containsNum and len(password) == 4 and not password.islower() and not password.isupper():
        return "Valid"
    else:
        return "Invalid"


def passwordCheck():
    with open("password.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            password = row[0]

    for i in range(3):
        print("First time? Password is 0000")
        guess = input("Type your password to log in: ")
        if guess == password:
            print("Welcome!")
            option()
    if guess != password:
        print("Login failed after 3 attempts.")


passwordCheck()
