# # To print my name in the termanal using dots
# # Aakash

# # Print "AAKASH" using stars

# letters = [
#     ["  *  ",
#      " * * ",
#      "*****",
#      "*   *",
#      "*   *"],

#     ["  *  ",
#      " * * ",
#      "*****",
#      "*   *",
#      "*   *"],

#     ["*   *",
#      "*  * ",
#      "***  ",
#      "*  * ",
#      "*   *"],

#     ["  *  ",
#      " * * ",
#      "*****",
#      "*   *",
#      "*   *"],

#     [" ****",
#      "*    ",
#      " *** ",
#      "    *",
#      "**** "],

#     ["*   *",
#      "*   *",
#      "*****",
#      "*   *",
#      "*   *"]
# ]

# # Print row by row
# for row in range(5):
#     for letter in letters:
#         print(letter[row], end="  ")
#     print()
    
#to print A password security system which detect user entered password and check whether it is valid or not, if not then give user 3 chances to enter a valid password. if the user entered wrong password 3 times then print "account locked"
password="Aakash@123"
chance=3    
while chance>0:
    user_password=input(" Enter a password: ")
    if user_password==password:
        print("password is correct")
        break
    else:
        chance -= 1
        print("password is incorrect. you have", chance, "chances left")
else:
    print("account locked")   
         