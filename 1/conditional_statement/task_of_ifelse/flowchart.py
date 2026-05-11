# question number:5

# from numpy import choose


# total_purchase_amount=int(input("Enter the total purchase amount:"))
# if total_purchase_amount>5000:
#     membership_status=input("do you have a membership card? (yes/no):")
#     if membership_status.lower()=="yes":
#         discount=(30/100)*total_purchase_amount
#         final_price=total_purchase_amount-discount
#         Total_saved=total_purchase_amount-final_price
#         print("you saved:", Total_saved)
#         print("The final price after discount is:",final_price)
#     else:
#         print("the final price without discount price is:", total_purchase_amount)
        
# else:
#     print("the final price without discount price is:", total_purchase_amount)
    
#question number:6
print("Welcome to the Magic Forest")
direction=input("Do you want to GO NORTH OR SOUTH?:")
if direction.lower()=="north":
    north=input("CROSS THE RIVER OR FOLLOW THE PATH?")
else:
    print("GAME OVER")
    
if north.lower()=="cross the river":
    print("GAME OVER")
else: 
    if north.lower()=="follow the path":
        choose=input("CHOOSE FAIR, OGRE OR ELF?")    
        if choose.lower()=="fairy":
            print("GAME OVER")
            print("END")
        elif choose.lower()=="ogre":
            print("GAME OVER")
        else:
            print("YOU WIN")
            print("GAME OVER")
            
            
# 4. Design a program for a 'Student Resource Portal.' The program should
# ask for a username and a password.
#  If the username is admin and password is ad123, print
# Access Granted: Faculty Dashboard.
#  If the username is student and password is st2026, print
# Access Granted: Notes and Practice Questions.
#  For any other combination, print Invalid Credentials.
# Please try again.

username=input("Enter your username:")
password=input("Enter your password:")
if username.lower()=="admin" and password=="ad123":
    print("Access Granted: Faculty Dashboard")
elif username.lower()=="student" and password=="st2026":
    print("Access Granted: Notes and Practice Questions")
else:
    print("Invalid Credentials. Please try again.")
     
    
# 7. Design a Traffic Light System. Given a variable light that can be red,
# yellow, or green, print the correct instruction. Also handle an invalid
# color with an error message.

light= ["red", "green", "yellow"]
if light=="red":
    print("STOP")
elif light=="green":
    print("GO") 
elif light=="yellow":
    print("GO SLOWLY")
else:
    print("INVALID COLOR")

# 8. Write a match statement that takes a number 1–4 and prints the
# corresponding season: 1=spring, 2=summer, 3=autumn, 4=winter.
# Default: unknown.

number=int(input("Enter number between 1-4"))
match number:
    case 1:
        print("SPRING")
    case 2:
        print("SUMMER")
    case 3:
        print("AUTUMN")
    case 4:
        print("WINTER")
    case _:
        print("UNKNOWN")
        

# 9. Design a Bank Loan Approval System. Approve a loan only if ALL three
# conditions are met:
#  Age is between 21 and 60 (inclusive)
#  Monthly income is at least 30,000
#  Credit score is at least 700
# If not approved, print which condition failed.

age=int(input("Enter your age:"))
monthly_income = int(input("Enter your monthly income:"))
credit_score=int(input("Enter your credit score:"))
if age>=21 and age<=60:
    if monthly_income>=30000:
        if credit_score>=700:
            print("Loan Approved")
        else:
            print("Loan Denied: Credit score is too low.")
    else:
        print("Loan Denied: Monthly income is too low.")
else:
    print("Loan Denied: Age is not within the eligible range.")

#10, Write a Python program that calculates a person’s Body Mass Index (BMI) and determines their weight category based on the following rules:
# Ask the user to input their weight as a float.
# Ask the user to input their height as a float.
# Calculate the BMI using the formula:

# BMI = weight / (height ** 2)

# Determine the weight category according to the following criteria:
# Underweight if BMI < 18.5
# Normal weight if 18.5 <= BMI < 25
# Overweight if 25 <= BMI < 30
# Obese if BMI >= 30
# Finally, print the result in the following format:

# Weight: 70
# Height: 1.75
# BMI: 22.9
# Category: Normal weight

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
bmi = weight / (height ** 2)
print(f"Weight: {weight}")
print(f"Height: {height}")
print(f"BMI: {bmi:.1f}")
if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 25:
    category = "Normal weight"
elif 25 <= bmi < 30:
    category = "Overweight"
else:
    category = "Obese"
print(f"Category: {category}")

# 11. You are developing a simple ticket booking system for a movie
# theatre. The ticket price depends on the age of the person and
# whether they have a membership card. If the person is under 12, the
# ticket is free. If the person is between 12 and 60: If they have a
# membership card, the ticket costs Rs. 150. If not, the ticket costs Rs.
# 200. If the person is above 60, they get a senior citizen discount,
# and the ticket costs Rs.
# 100. Write a Python program using nested if-else to calculate and print
# the ticket price based on the user's age and membership status.
                                    
# 12. A company decided to give bonus of 5% to employee if his/her
# year of service is more than 5years. Ask user for their salary and year
# of service and print the net bonus amount.

age=int(input("Enter your age:"))
membership_card=input("Do you have membership card?(yes/no):").lower()
if age<12:
    print("Your ticket is free")
elif 12<=age<=60:
    if membership_card=="yes":
        ticket_cost=150
    else:
        ticket_cost=200
        print("the cost of ticket is",ticket_cost)
elif age>60:
    print("you get the citizen discoun of Rs 100")
    price=100
    print("the cost of ticket after discount is",price)
else:
    print("you don't meet the ticket_requirement")



# 13. Write a python program which accepts the radius of circle from
# user and compute the area.
radius=float(input("Enter radius of circle"))
area=(22/7)*radius**2
print("the area if the circle is", area)


"""14,
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

# 15. Accept input from user
# If given number is a multiple of both 3 and 5 prints Fizz Buzz instead
# of number
# If given number is a multiple of 3 but not 5 prints Fizz instead of
# number
# If given number is a multiple of 5 but not 3 prints Buzz instead of
# number
# If given number is not multiple of 3 or 5 prints value as usual.

number=int(input("Enter a number:"))
if number%3==0 and number%5==0:
    print("Fizz Buzz")
elif number%3==0 and number%5!=0:
    print("Fizz")
elif number%5==0 and number%3!=0:
    print("Buzz")
else:
    print("the given number is not multiple of 3 or 5, the value is", number)

# 16. A utility company charges different rates based on electricity
# usage:
# If usage < 100 units then cost Rs 5 per unit
# If usage is between 100 to 300 units:
# First 100 units: Rs 5
# Next units: Rs 8
# If usage is > 300 units: First 100: Rs 5 Next 200: Rs 8 Remaining: Rs
# 10

uints=int(input("Enter your electricity usage in units: "))
if uints<100:
    cost=uints*5
elif 100<=uints<=300:
    cost=100*5 + (uints-100)*8
else:
    cost=100*5 + 200*8 + (uints-300)*10
print("The cost of electricity is Rs", cost)

# 17. Write a complete Python program that:
#  Asks Player 1 to enter their move ( input: rock, paper, or
# scissors)
#  Asks Player 2 to enter their move ( input: rock, paper, or
# scissors)
#  Prints who wins or if it's a tie

player1_move=input("Player 1, enter your move (rock, paper, or scissors):").lower()
player2_move=input("Player 2, enter your move (rock, paper, or scissors):").lower()
if player1_move==player2_move:
    print("It's a tie!")
elif (player1_move=="rock" and player2_move=="scissors") or (player1_move=="paper" and player2_move=="rock") or (player1_move=="scissors" and player2_move=="paper"):
    print("Player 1 wins!")
else:
    print("Player 2 wins!")
    


# 18. Write a Python program that takes a number as input, first
# checks if it is positive if yes then check whether it is even or odd

number=int(input("Enter a number:"))
if number>0:
    if number%2==0:
        print("The number is positive and even.")
    else:
        print("The number is positive and odd.")
else:
    print("The number is not positive.")

# 19. A store gives a 20% discount if the total purchase is above RS
# 1000 AND the customer is a member, or a 10% discount if the
# purchase is above RS 1000 but the customer is not a member. Write a
# program that takes total_amount and is_member (True/False) as
# input and prints the final amount after applying the correct discount
# or no discount.

total_amount=float(input("Enter the total purchase amount:"))
is_member=input("Are you a member? (yes/no):").lower()
if total_amount>1000 and is_member=="yes":
    discount=0.20*total_amount
    final_amount=total_amount-discount
    print("You get a 20% discount. Final amount is Rs", final_amount)
elif total_amount>1000 and is_member!="yes":
    discount=0.10*total_amount
    final_amount=total_amount-discount
    print("You get a 10% discount. Final amount is Rs", final_amount)
else:
    print("No discount applied. Final amount is Rs", total_amount)
    
"""
20. Create a weight conversion program that:
Asks the user what their Earth weight is as a float. Asks
the user for a planet number as an int.

Then, use an if/elif/else statement to calculate the user’s weight on
the destination planet.

To calculate the user’s weight:
destination weight = Earth weight × relative gravity

Number    Planet    Relative Gravity
1         Mercury   0.38
2         Venus     0.91
3         Mars      0.38
4         Jupiter   2.53
5         Saturn    1.07
6         Uranus    0.89
7         Neptune   1.14

If the user enters a planet number outside of 1 - 7, print a message
that says "Invalid planet number"
"""
earth_weight=float(input("Enter your Earth weight in kg:"))
planet_number=int(input("Enter a planet number (1-7):"))
if planet_number==1:
    relative_gravity=0.38
elif planet_number==2:
    relative_gravity=0.91
elif planet_number==3:
    relative_gravity=0.38
elif planet_number==4:
    relative_gravity=2.53   
elif planet_number==5:
    relative_gravity=1.07
elif planet_number==6:  
    relative_gravity=0.89               
elif planet_number==7:
    relative_gravity=1.14
else:   
    print("Invalid planet number")
destination_weight=earth_weight*relative_gravity
print(f"Your weight on the destination planet is: {destination_weight:.2f} kg")

    

# 21. WAP which accepts marks of four subjects and display total
# marks, percentage and grade. Hint: more than 70 –> distinction, more
# than 60 –> first, more than 40 –> pass, less than 40 –> fail

marks=input("Enter marks of four subjects separated by space:").split()
marks=[float(mark) for mark in marks]   
total_marks=sum(marks)
percentage=(total_marks/400)*100
print("Total Marks:", total_marks)
print("Percentage:", percentage)
if percentage>70:
    grade="Distinction"
elif percentage>60:
    grade="First"
elif percentage>40:
    grade="Pass"
else:
    grade="Fail"
print("Grade:", grade)

# 22. Write a program that simulates the elevator's internal logic. The
# program should accept user inputs for the desired floor, the current weight
# load, and the door status, then determine if the elevator is cleared to move.
# Requirements
# Target Floor: An integer representing the user's selection.
# Total Weight: A numerical value (in kg) representing the current load inside
# the lift.
# Door Status: A Boolean or string indicating whether the door is closed or
# open.
# Logic Constraints
# Floor Validation
#  The elevator only services floors in the range of 0 to 10.
#  If the input is outside this range, the system must display
# INVALID FLOOR and terminate the process.
# Weight Limit Sensor
#  The safety limit for this lift is 500kg.
#  If the total weight is greater than 500kg, the system must
# display OVERWEIGHT: LIFT CANNOT MOVE and terminate.
# Door Mechanism Status
#  The lift cannot move unless the door is fully engaged/closed.
#  If the door is open, display WARNING: CLOSE THE DOOR and
# terminate.
# If all three conditions are met, the program should output: ACTIVATE
# ELEVATOR MOTION.

target_floor=int(input("Enter the target floor (0-10):"))
if target_floor<0 or target_floor>10:
    print("INVALID FLOOR")
elif target_floor>=0 and target_floor<=10:
    total_weight=float(input("Enter the total weight load in kg:"))
    if total_weight>500:
        print("OVERWEIGHT: LIFT CANNOT MOVE")
    else:
        door_status=input("Is the door closed? (yes/no):").lower()
        if door_status!="yes":
            print("WARNING: CLOSE THE DOOR")
        else:
            print("ACTIVATE ELEVATOR MOTION")
else:  
    print("Invalid input for target floor.")


    

# 23. Write a Python program to simulate a simple ATM with the
# following specifications: Assume the card is valid (is_valid = True)
#  Initial account balance is RS 5000
#  Correct PIN is 123
#  After entering correct PIN, display the menu:
# 1. Withdraw
# 2. Check Balance
# 3. Exit
#  If user selects 1 then ask amount and deduct from balance
#  If user selects 2 then show current balance
#  If user selects 3 then print Thank you for visiting
# Show proper messages for wrong PIN and invalid option

is_valid = True
account_balance = 5000
if is_valid:
    pin = int(input("Enter your PIN: "))
    if pin == 123:
        print("Menu:")
        print("1. Withdraw")
        print("2. Check Balance")
        print("3. Exit")
        option = int(input("Select an option (1, 2, or 3): "))
        if option == 1:
            amount = float(input("Enter the amount to withdraw: "))
            if amount <= account_balance:
                account_balance -= amount
                print(f"Withdrawal successful. Current balance: Rs {account_balance}")
            else:
                print("Insufficient balance.")
        elif option == 2:
            print(f"Current balance: Rs {account_balance}")
        elif option == 3:
            print("Thank you for visiting.")
        else:
            print("Invalid option selected.")
    else:
        print("Wrong PIN.")
else:
    print("Invalid card.")
