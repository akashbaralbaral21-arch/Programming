# 3. Generate a frequency table for the rating list which is initialized below:
# Ratings=["4+","9+","12+","17+","4+","12+","4+","9+","17+","12+","4+","17+"]
# a. start by creating an empty dictionary named content_rating
# b. Loop through the ratings list. for each rating list. for each iteration, complete the following
# if the rating is already is already in content_rating then increment the frequency of that ration by 1
# else, initialize the frequency with a value of 1 inside the content_rating dictionary

# Ratings=["4+","9+","12+","17+","4+","12+","4+","9+","17+","12+","4+","17+"]
# content_rating={}
# while i<len(Ratings):
#     rating=Ratings[i]
#     if rating in content_rating:
#         content_rating[rating] += 1
#     else:
#         content_rating[rating] = 1
#     i+=1
# print(content_rating)

# # write the program to generate a random number between 1 to 10 and prompt the user to guess the number. Use a while loop to keep asking the user until they guess the correct number. Provide feedback if the guess is too low or too high.
# import random
# number=random.randint(1,10)
# guess=None

# while guess != number:
#     guess=int(input("Guess the number between 1 and 10: "))
#     if guess < number:
#         print("Too low, try again.")
#     elif guess > number:
#         print("Too high, try again.")
# print("Congratulations! You guessed the number.")


# # write a python program that simulates a login system. the program should prompt the user to enter a username and password. if both are correct. print lofin successful and exit,if either is incorrect, print invalid credentials , try again. allow the usder up to 3 attamps before locking them our with the message too many failed attemprs\
# username="admin"
# password="password123"
# attempts=0
# while attempts < 3:
#     entered_username=input("Enter your username: ")
#     entered_password=input("Enter your password: ")
#     if entered_username == username and entered_password == password:
#         print("Login successful!")
#         break
#     else:
#         print("Invalid credentials, try again.")
#         attempts += 1
# else:
#     print("Too many failed attempts. You are locked out.")
    
    
# count=0 
# while count<3:
#     name=input("enter a name:")
#     if name != "good luck" and name != "Good Luck" and name != "GOOD LUCK":
#         print(f"try again, you have enterd {name}")
#     else:
#         count+=1 
#         print(f'You have entered good luck,{count} times')
        
# print("Congratulations! You have entered good luck 3 times.")

import random
number=random.randint(1,51)
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
    if attempts==0:
        print("Sorry, you have used all your attempts. The number was:", number)
        

        
    
