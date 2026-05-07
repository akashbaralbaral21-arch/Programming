# 1,A theme park has these rules: You can ride the roller coaster if you are at least 12 years old AND at least 140 cm tall. Write the if-else code for this.

age = input("enter your age")
height = int(input("enter your height"))

if age>=12 and height >=140:
    print("You can ride the roller coaster")
else:
    print("You can't ride the roller coaster")

# 2,Design a Traffic LIGHT System. Given a variable light that can be "red", "yellow" or "green", print the correct instruction. Also handle an invalid color with an error message.

light= ["red" "green" "yellow"]
if light=="red":
    print("STOP")
elif light=="green":
    print("GO")
elif light=="yellow":
    print("GO SLOWLY")
else:
    print("INVALID COLOR")

# 3, WRITE A MATCH STATEMENT THAT TAKES A NUMBER 1-4 AND PRINTS THE CORRESPONDING SEASON:
#   1=SPRING, 2=summer, 3=autumn, 4=winter. Default:"unknown".


number=int(input("Enter number between 1-4"))
match number:
    case 1:
        print("SPRING SEASON")
    case 2:
        print("SUMMER")
    case 3:
        print("AUTUMN")
    case 4:
        print("WINTER")
    case _:
        print("UNKNOWN")
        
# 4,Write a ligin system using nested if. Check:
#            *if username eqals "admin"
#            *inside that, if password equals "pass123"
#         Print appropriate messages for: valid login, wrong password, wrong username.

username = "admin"
password = "pass123"
entered_username = input("Enter your username")
entered_password = input("Enter your password")
if entered_username == username:    
    if entered_password == password:
        print("Valid login")
    else:
        print("Wrong password")
else:   
    print("Wrong username")
            
# 5,Design a Bank Loan Approval System. Approve a loan only if ALL three conditions are met:
# * Age is between 21 and 60 (inclusive)
# *Monthly income ia at least 30,000
# *Credit score is at least 700
# if not approved, print which condition failed, if multiple fail, pick the most important one to report.


age=int(input("Enter your age"))
monthly_income = int(input("Enter your monthly income"))
credit_score=int(input("Enter your credit socore"))


if age>=21 and age<=60:
    if monthly_income>=30000:
        if credit_score>=700:
            print("Loan Approved")
        else:
            print("Credit score is too low")
    else:
        print("Monthly income is too low")
else:
    print("Age is not within the required range")   
    
    
6, # You are developing a simple ticket booking system for a movie theater. The ticket price depends on the age of the person and whether they have a mimbership card. if the person is under 12, the ticket is free. if the person is between 12 and 60: if they have a membership card, the ticket costs Rs.150. if not, the ticket costs Rs.200. if the person is above 60, they get a senior citizen dicount, and the ticket costs Rs. 100. Write a python program using nested if-else to calculate and print the ticket price based ont he user's age and membership status

age=int(input("Enter your age"))
membership_card = input("Do you have a membership card? (yes/no)")
if age<12:
    print("The ticket is free")
elif age>=12 and age<=60:
    if membership_card.lower()=="yes":
        print("The ticket costs Rs.150")
    else:
        print("The ticket costs Rs.200")
else:
    print("The ticket costs Rs.100")
                

#7, A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. Ask for their salary and year of service and print the net bonus amount.

salary = int(input("Enter your salary"))
years_of_service = int(input("Enter your years of service"))
if years_of_service>5:
    bonus = salary*0.05
    print("Your net bonus amount is: ", bonus)
else:   
    print("You are not eligible for a bonus")

                                
#8, Write a pyton program which accepts the radus of the circle from user and compute the area.
import math
radius = float(input("Enter the radius of the circle"))
area = math.pi*radius**2
print("The area of the circle is: ", area)

"""
9,
Accept the age, gender ('M', 'F'), and number of days from the user 
and display the wages accordingly based on this table:

Age Range          | Gender | Wage/day
-------------------|--------|---------
>= 18 and < 30     | M      | 700

                   | F      | 750
-------------------|--------|---------
>= 30 and <= 40    | M      | 800

                   | F      | 850
"""
age = int(input("Enter your age"))
gender = input("Enter your gender (M/F)")
if age>=18 and age<30:
    if gender.upper()=="M":
        print("Your wage/day is: 700")
    elif gender.upper()=="F":
        print("Your wage/day is: 750")  
elif age>=30 and age<=40:
    if  gender.upper()=="M":
        print("Your wage/day is: 800")
    elif gender.upper()=="F":
        print("Your wage/day is: 850")      
else:
    print("You are not eligible for a wage")

"""10, Accept input from user
       if given number is multiple of both 3 and 5 prints "FizzBuzz" instead of number
       if given number is amultiple of 3 but not 5 prints "Fizz" instead of number
       if given number is a multiple of 5 but not 3 prints "Buzz" instead of number
       if given number is not multiple of 3 or 5 prints value as usual
       
"""
number = int(input("Enter a number"))
if number%3==0 and number%5==0:
    print("FizzBuzz")
elif number%3==0 and number%5!=0:
    print("Fizz")
elif number%5==0 and number%3!=0:
    print("Buzz")   
else:   
    print(number)


     


