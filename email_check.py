# checking email address

import re

my_email = str(input("Type your email address:"))
my_password = input("Type your password:")

email_list= ("simple@example.com", "very.common@example.com", "disposable.style.email.with+symbol@example.com",
           "other.email-with-hyphen@example.com", "fully-qualified-domain@example.com",
           "user.name+tag+sorting@example.com", "x@example.com","example-indeed@strange-example.com",
           "test/test@test.com", "admin@mailserver1",
           "example@s.example", "@example.org", "john..doe@example.org", "mailhost!username@example.org",
           "user%example.com@example.org", "user-@example.org",	"postmaster@[123.123.123.123]",
           "postmaster@[IPv6:2001:0db8:85a3:0000:0000:8a2e:0370:7334]","Abc.example.com", "A@b@c@example.com",
           "ab(c)d,e:f;g<h>i[j\k]l@example.com", "justnotright@example.com", "this isnot\allowed@example.com",
           "this\ still\"not\\allowed@example.com", "1234567890123456789012345678901234567890123456789012345678901234+x@example.com",
            "i_like_underscore@but_its_not_allowed_in_this_part.example.com", "QA[icon]CHOCOLATE[icon]@test.com")

def email_check(email_address):
    print(email_address)
    if re.fullmatch("[a-zA-Z0-9_.-]*@[a-zA-Z0-9-]*.[a-z]*", email_address):
        print("email ok")
    else:
        print("wrong email")

def password_check(password):
    if


for i in email_list:
    email_check(i)
