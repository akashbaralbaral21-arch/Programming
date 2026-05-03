# write a program to check whether the given number is in between 1 to 100 or not.

number = int(input("Enter a number:"))
if number > 1 and number < 100:
    print(f"{number} is in between 1 and 100");
    
else:
    print(f"{number} is not in between 1 and 100");


#2 check whether the user input number is even or odd
number = int(input("Enter a number:"))
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")


#3 write a program that asks the user for a number in the range of 1 to 12

month = int(input("Enter a month number (1-12): "))
if month ==1:
    print("Janaury")
    
elif month ==2:
    print("February")
elif month==3:
    print('March:')
elif month == 4:
    print("April")
elif month==5:
    print("May")
elif month ==6:
    print("June")
elif month ==7:
    print("July")
elif month == 8:
    print ("August")
elif month ==9:
    print('september')
elif month == 10:
    print("October")
elif month == 11:
    print ( "November")
elif month== 12:
    print("December")
else:
    print("entered a invalid month number")
    

#using dictinory
month={1:"January", 2:"February", 3:"March", 4:"April", 5:"May", 6:"June", 7:"July", 8:"August", 9:"September", 10:"October", 11:"November", 12:"December"}
month_number = int(input("Enter a month number (1-12): "))
if month_number in month:
    print(month[month_number])              
else:    
    print("entered a invalid month number")

# write a program to accept two number and mathmatical operators and perform operations according to the operator
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operator = input("Enter an operator (+, -, *, /): ")
if operator == "+":
    print(f"The sum of {num1} and {num2} is {num1 + num2}")
elif operator == "-":
    print(f"The difference of {num1} and {num2} is {num1 - num2}")
elif operator == "*":
    print(f"The product of {num1} and {num2} is {num1 * num2}")
elif operator == "/":
    if num2 != 0:
        print(f"The quotient of {num1} and {num2} is {num1 / num2}")
    else:
        print("Error: Division by zero is not allowed.")
else:   
    print("Invalid operator entered.")

                                            
# write a  python program to check car loan eligibility: 
#   Salary >= 50,000 and Credit Score >= 700: "Eligible"
# Otherwise: "Not Eligible"

salary = (input("enter your salary:"))
credit_score = (input("enter your credit score: "))

if salary>= 50000 and credit_score >=700:
    print("he is eligible for car loan")
else:
    print("he is not eligible for car loan")
    



#         8. Write a Python program that takes an integer input n n. 

#         From given number, 

#         check if it is divisible by both 3 and 5, and print "FizzBuzz" 

#         if true. 

#         If the number is divisible only by 5, print "Buzz." If it is 

#         divisible only by 3, print "Fizz." 

#         Finally, if the number is not divisible by either 3 or 5, 

#         print the number itself.

n = int(input("Enter an integer: "))
if n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")
elif n % 5 == 0:
    print("Buzz")
elif n % 3 == 0:
    print("Fizz")
else:
    print(n)

# 9. Write a Python program that takes a character input and 

# checks whether it is a vowel or consonant.

input_char = input("Enter a character: ").lower()
if input_char in ['a', 'e', 'i', 'o', 'u']:
    print(f"{input_char} is a vowel.")  
elif input_char.isalpha():
    print(f"{input_char} is a consonant.")
else:
    print("Invalid input. Please enter a single alphabetic character.")




# 10. Write a Python program to input marks and determine the grade based on the following conditions:

# 90-100: A

# 80-89: B

# 70-79: C

# Below 70: Fail

marks = int(input("Enter marks: "))
if marks >= 90 and marks <= 100:
    print("Grade: A")
elif marks >= 80 and marks < 90:
    print("Grade: B")
elif marks >= 70 and marks < 80:
    print("Grade: C")
elif marks < 70:
    print("Grade: Fail")
    



# 11. Write a Python program to categorize a person’s age:

# Age < 13: Child

# 13 <= Age <= 19: Teenager

# Age > 19: Adult
age = int(input("Enter age: "))
if age < 13:
    print("Child")
elif age >= 13 and age <= 19:
    print("Teenager")
elif age > 19:
    print("Adult")
    



# 12.Write a Python program to check if a given character is uppercase, lowercase, or a digit.

input_char = input("Enter a character: ")
if input_char.isupper():
    print(f"{input_char} is an uppercase letter.")  
elif input_char.islower():
    print(f"{input_char} is a lowercase letter.")
elif input_char.isdigit():
    print(f"{input_char} is a digit.")
else:
    print("Invalid input. Please enter a single character.")
    
    



# 13. Write a Python program that takes a color as input ("Red", "Yellow", "Green") and outputs the corresponding action ("Stop", "Get Ready", "Go").
color = input("Enter a traffic light color (Red, Yellow, Green): ").lower()
if color == "red":
    print("Stop")
elif color == "yellow":
    print("Get Ready")
elif color == "green":
    print("Go")
else:
    print("Invalid color entered. Please enter Red, Yellow, or Green.")




# 14. Write a Python program to check eligibility for a job based on age and experience:

# Age > 18 and Experience >= 2 years: Eligible

# Otherwise: Not Eligible

age = int(input("Enter your age: "))
experience = int(input("Enter your years of experience: "))
if age > 18 and experience >= 2:
    print("Eligible for the job")
else:
    print("Not eligible for the job")

                                            



# 15. Write a Python program to give advice based on the temperature:

# Temperature > 30°C: "It's hot, stay hydrated!"

# Temperature between 15-30°C: "Enjoy the weather!"

# Temperature < 15°C: "It's cold, wear warm clothes!"
temperature = float(input("Enter the temperature in Celsius: "))
if temperature > 30:
    print("It's hot, stay hydrated!")
elif temperature >= 15 and temperature <= 30:
    print("Enjoy the weather!")
elif temperature < 15:
    print("It's cold, wear warm clothes!")
else:
    print("Invalid temperature entered.")
    




# 16. Write a Python program that takes a menu option ("Pizza", "Burger", "Pasta") and prints its price:

# Pizza: $10

# Burger: $7

# Pasta: $8

menu_option = input("Enter a menu option (Pizza, Burger, Pasta): ").lower()
if menu_option == "pizza":
    print("Price: $10")
elif menu_option == "burger":
    print("Price: $7")
elif menu_option == "pasta":
    print("Price: $8")
else:
    print("Invalid menu option entered. Please enter Pizza, Burger, or Pasta.")



# 17. Write a Python program to select players based on height:

# Height >= 6 feet: Selected

# Height < 6 feet: Not Selected
height = float(input("Enter height in feet: "))
if height >= 6:
    print("Selected")
else:
    print("Not Selected")



# 18. Write a Python program to check if a person is eligible to watch a movie based on their age:

# Age >= 18: Allowed

# Age < 18: Not Allowed 
age = int(input("Enter your age: "))
if age >= 18:
    print("Allowed to watch the movie")
else:
    print("Not allowed to watch the movie") 




# 19. Write a Python program to check login credentials:

# Username: "admin", Password: "password123"

# If correct, print "Access Granted"; otherwise, print "Access Denied."
username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin" and password == "password123":
    print("Access Granted")
else:
    print("Access Denied")  

                



# 20. Write a Python program that takes a month number (1–12) and outputs the corresponding season:

# 12, 1, 2: "Winter"

# 3, 4, 5: "Spring"

# 6, 7, 8: "Summer"

# 9, 10, 11: "Autumn"

month_number = int(input("Enter a month number (1-12): "))

if month_number in [12, 1, 2]:
    print("Winter") 
elif month_number in [3, 4, 5]:
    print("Spring")
elif month_number in [6, 7, 8]: 
    print("Summer")
elif month_number in [9, 10, 11]:   
    print("Autumn") 
else:
    print("Invalid month number entered. Please enter a number between 1 and 12.")
        
  
