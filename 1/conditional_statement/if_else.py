temperature= 35
if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")
    
    
    
score= 85
if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
else:
    print("Grade D")    


#without if else
balance = 1000
amount = int(input("Enter the amount to withdraw: "))
balance= balance - amount
print("Your remaining balance is: ", balance)

#with if else
balance = 1000
amount = int(input("Enter the amount to withdraw: "))
if amount > balance:
    print("Insufficient balance")
else:
    balance= balance - amount
    print("Your remaining balance is: ", balance)

                    
username = "admin"
password = "admin123"
    
entered_username = "admin123"
entered_password = "admin123"
if entered_username == username  and entered_password == password:
    print("Login successful")
    
else:
    print("Invalid username or password")




marks = 45

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Grade: F")

#without if else
name="ram"
age = 14

print(f"{name} registered to vote")
print("voter id issued")

#with if else
name="ram"
age = 14
if age >= 18:
    print(f"{name} registered to vote")
    print("voter id issued")
else:
    print(f"{name} is not eligible to vote")

                            
                            