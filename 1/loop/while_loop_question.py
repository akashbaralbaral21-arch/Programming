# #1.
# total=0
# while (number:= int(input("Enter a number: "))) != 0:
#     total += number
# print("The sum of the numbers is:", total)

# #2.write a program that takes a positive integer n as input and counts down form n to 1 using awhile loop, printing each number. when it reaches 1, print"Lower threshold reached"
# n = int(input("Enter a positive integer: "))
# while n > 0:
#     print(n)
#     n -= 1
# print("Lower threshold reached")

# #3. Generate a random number between 1 and 100, and ask the user to guess it repetedly using a while loop until they guess correctly.
# import random
# number = random.randint(1, 100)
# guess = None
# i=0
# while guess != number:
#     guess = int(input("Guess the number between 1 and 100: "))
#     i=i+1
#     if guess < number:
#         print("Too low, try again.")
#     elif guess > number:
#         print("Too high, try again.")
# print("Congratulations! You guessed the number.")
# print(f"You guessed the number in {i} attempts.")

# #4. write a program that prompts the user to enter a password. Keep asking until the password meets criteria greater than 8 characters. Display a security alert passowrd must be 8+ characetrs.

# password = input("Enter your password: ")
# while len(password) < 8:
#     print("Password must be at least 8 characters long. Please try again.")
#     password = input("Enter your password: ")
# print("Password accepted. Welcome to the system!")

# 5. Write a program that calculates the sum of all even numbers form 1 to 5o using a while loop.
# Requirements:
#     a) Initialize a total variable to o.
#     b) Initalize a counter variable at 1.
#     c) The loop should stop once the counter exceeds 50.Warning
#     d) Print only the final sum at the very end.
# total = 0
# counter = 1
# while counter <=50:
#     if counter %2==0:
#         total += counter
#     counter += 1
# print("The sum of all even number form 1 to 50 is:",total)
# print("the total even number is:",counter//2)

#6. Take a number and use a while loop to print its multiplication table.
# number=int(input("Enter a number:"))
# i=1
# while i<11:
#     print(f"{number} x {i} = {number*i}")
#     i+=1
    
# print("these are the multiplication table of", number)

#8. Generate a random number (1-50). Give the user up to 7 attempts to guess it using a while loop. Track remaining attempts and stop early if they guess correctly or run out of tries.
import random
number=random.randint(1,50)
attempts=7
count=0
while attempts > 0 and attempts <= 7:
    guess=int(input("Guess the number between 1 and 50: "))
    if guess == number:
        print("Congratulations! You guessed the number.")
        print(f"you guessed in {count} times")
        break
    elif guess < number:
        print("Too low, try again.")
    else:
        print("Too high, try again.")
    attempts -= 1
    count += 1
    print(f"You have {attempts} attempts remaining.")
if attempts == 0:
    print("Sorry, no more attempt left.")
    
