# checking email address and password

import re

my_email = str(input("Type your email address:"))
my_password = input("Type your password:")


def email_check(email_address):
    print(email_address)
    if re.fullmatch("[a-zA-Z0-9_.-]*@[a-zA-Z0-9_.-]*\\.[a-z]{2,5}", email_address):
        print("Correct email format")
    else:
        print("Wrong email format")


def password_check(password):
    print(password)
    check_lc = re.search("[a-z]+", password)
    check_uc = re.search("[A-Z]+", password)
    check_num = re.search("[0-9]+", password)
    check_length = re.search("^.{8,20}$", password)
    check_specials = re.search("[~!@#$%^&*()_+={}|:;<>.,?/\\\\\\-]+", password)
    if check_lc and check_uc and check_num and check_length and check_specials:
        print("Password is strong enough")
    else:
        print("Password is too weak")


email_check(my_email)
password_check(my_password)
