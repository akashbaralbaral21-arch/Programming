first_name=input("Enter your first name: ")
if first_name=="":
    print("first name cannot be empty")
elif not first_name.isalpha():
    print("first name cannot contain numbers")
else:
    print("valid")

# last name: not empty + letters only

last_name=input("Enter your last name:")
if last_name == "":
    print("Last name cannot be empty")
elif not last_name.isalpha():
    print("Last name must be alphabetic")
else:
    print('Valid last name')
    
# Email.contains @ and . 
email=input("Enter your email:")
if "@" not in email or "." not in email:
    print("Invalid email address")
else:
    print("valid email address")
    
    
# re-email: matches first email

re_email = input("Re-enter your email:")
if re_email != email:
    print("Email adresses do not match")
else:
    print("Email addresses match")
    
# password minimun 6 charecters
password = input("Enter you password:")
if len(password) < 6:
    print("Password must be at least 6 characters long")
else:
    print("Valid password")
    
# Alternative of doing the same thing in more easy and faster way
first_name=input("Enter your first name:")
last_name=input("Enter your last name:")
email=input("Enter your email:")
re_email=input("enter your email again:")
password=input("Enter you password:")

if not first_name == "" and last_name == "" and email == "" and re_email == "" and password == "":
    if first_name.isalpha() and last_name.isalpha():
        if "@" in email and "." in email:
            if email == re_email:
                if len(password) >= 6:
                    print("All inputs are valid")
                else:
                    print("Password must be at least 6 characters long")
            else:
                print("Email addresses do not match")
        else:
            print("Invalid email address")
    else:
        print("First name and last name must be alphabetic")
