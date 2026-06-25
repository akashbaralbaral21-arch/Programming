# While Loop Exercises
# # 1. Write a program that prompts the user to input a series of numbers until they
# input a duplicate number. Use a while loop to check for duplicates.
numbers = []
while True:
    num = int(input("Enter a number: "))
    if num in numbers:
        print("Duplicate number entered:", num)
        break
    numbers.append(num)
print("Numbers entered:", numbers)


# 2. Write a program that prompts the user to enter a positive integer. It then
# calculates and prints the factorial of that number using a while loop.
num = int(input("Enter a positive integer: "))
factorial = 1
i = 1
while i <= num:
    factorial = factorial * i
    i += 1
print("Factorial:", factorial)


# 3. Write a program that accepts a number from the user and calculates the sum of
# all numbers from 1 up to that number.
num = int(input("Enter a number: "))
total = 0
i = 1
while i <= num:
    total = total + i
    i += 1
print("Sum:", total)


# 4. Given a list of numbers, use a loop to count how many times a specific number for
# example 10 appears.
numbers = [10, 20, 10, 30, 10, 40, 10]
count = 0
i = 0
while i < len(numbers):
    if numbers[i] == 10:
        count += 1
    i += 1
print("10 appears", count, "times")


# 5. Write a program that counts the total number of vowels and consonants in a given
# sentence, ignoring spaces and special characters.
sentence = input("Enter a sentence: ")
vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0
i = 0
while i < len(sentence):
    ch = sentence[i]
    if ch.isalpha():
        if ch in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
    i += 1
print("Vowels:", vowel_count)
print("Consonants:", consonant_count)


# 6. Write a program to count the total number of digits in a given integer.
num = int(input("Enter an integer: "))
n = abs(num)
count = 0
if n == 0:
    count = 1
while n > 0:
    n = n // 10
    count += 1
print("Number of digits:", count)


# 7. Generate a sequence until it reaches 1. If you start with any positive integer n, and
# if n is even, divide it by 2; if n is odd, multiply it by 3 and add 1. Repeat the process.
# The sequence will always eventually reach 1. Write a program to print this
# sequence for a given number.
# given input: n = 6
# expected output: 6, 3, 10, 5, 16, 8, 4, 2, 1
n = int(input("Enter a positive integer: "))
print(n, end="")
while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = n * 3 + 1
    print(",", n, end="")
print()


# 8. Print alphabet Series from A-Z
ch = ord('A')
while ch <= ord('Z'):
    print(chr(ch), end=" ")
    ch += 1
print()


# 9. Write a program that prompts the user for a starting integer and an ending integer.
# Use a while loop to print all numbers between them, inclusive.
start = int(input("Enter starting integer: "))
end = int(input("Enter ending integer: "))
i = start
while i <= end:
    print(i, end=" ")
    i += 1
print()


# 10. Write a program that prints all odd numbers between 1 and 50 in descending
# order from 49 down to 1 using a while loop.
n = 49
while n >= 1:
    print(n, end=" ")
    n -= 2
print()


# 11. Write a program that prints all multiples of 7 between 1 and 100.
n = 7
while n <= 100:
    print(n, end=" ")
    n += 7
print()


# 12. Write a program that continuously prompts the user to input numbers. The loop
# should terminate immediately when the user enters 0. Afterward, print the total
# sum of all numbers entered excluding the 0.
total = 0
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    total += num
print("Total sum:", total)


# 13. Write a program that asks a user to enter their age. If the input is less than 0 or
# greater than 120, print invalid age and prompt them again. The loop should
# repeat until a valid age is provided.
while True:
    age = int(input("Enter your age: "))
    if age < 0 or age > 120:
        print("Invalid age")
    else:
        print("Valid age:", age)
        break


# 14. Write a program that allows a teacher to input student scores one by one. The loop
# ends when the teacher types -1. The program should then calculate and display
# the average score.
total = 0
count = 0
while True:
    score = float(input("Enter score (-1 to stop): "))
    if score == -1:
        break
    total += score
    count += 1
if count > 0:
    print("Average score:", total / count)
else:
    print("No scores entered.")


# 15. Write a program that simulates a login screen. Give the user a maximum of 3
# attempts to type the correct password for example secret123. If they fail 3 times,
# print access denied, if they succeed early, print access granted and exit the loop.
password = "secret123"
attempts = 0
while attempts < 3:
    entered = input("Enter password: ")
    if entered == password:
        print("Access granted")
        break
    else:
        attempts += 1
        print("Wrong password.")
else:
    print("Access denied")


# 16. Write a program that takes an integer input and constructs a new integer that is
# the exact reverse of the input for example input is 582 outputs the actual integer
# 285.
num = int(input("Enter an integer: "))
n = abs(num)
reversed_num = 0
while n > 0:
    digit = n % 10
    reversed_num = reversed_num * 10 + digit
    n = n // 10
print("Reversed:", reversed_num)


# 17. Write a program that uses a while loop to print the first n terms of the Fibonacci
# sequence 0, 1, 1, 2, 3, 5, 8 where n is provided by the user.
n = int(input("How many terms? "))
a = 0
b = 1
count = 0
while count < n:
    print(a, end=" ")
    temp = a + b
    a = b
    b = temp
    count += 1
print()


# 18. Write a program that loops through a string using a while loop and prints a new
# version of the string with all the vowels removed.
string = input("Enter a string: ")
vowels = "aeiouAEIOU"
result = ""
i = 0
while i < len(string):
    if string[i] not in vowels:
        result += string[i]
    i += 1
print("Without vowels:", result)


# 19. Write a program that scans a string using a while loop index to count how many
# times the specific two-character substring hi appears.
string = input("Enter a string: ")
count = 0
i = 0
while i < len(string) - 1:
    if string[i] == 'h' and string[i + 1] == 'i':
        count += 1
    i += 1
print("'hi' appears", count, "times")


# 20. Write a program to find and print all numbers in the list that are multiples of 5.
# numbers = [12, 25, 7, 30, 18, 40, 55, 9]
numbers = [12, 25, 7, 30, 18, 40, 55, 9]
i = 0
while i < len(numbers):
    if numbers[i] % 5 == 0:
        print(numbers[i], end=" ")
    i += 1
print()


# 21. Write a program that processes a string character by character using a while loop,
# converting all lowercase letters to uppercase and vice versa.
string = input("Enter a string: ")
result = ""
i = 0
while i < len(string):
    if string[i].isupper():
        result += string[i].lower()
    elif string[i].islower():
        result += string[i].upper()
    else:
        result += string[i]
    i += 1
print("Result:", result)


# 22. For every single increment of the outer loop i, how many times does the inner loop
# j run?
# i = 1
# while i <= 2:
#     j = 1
#     while j <= 2:
#         print(f'({i},{j})', end=' ')
#         j += 1
#     i += 1
# Answer: j runs 2 times for every single increment of i
i = 1
while i <= 2:
    j = 1
    while j <= 2:
        print(f'({i},{j})', end=' ')
        j += 1
    i += 1
print()


# 23. Why does this code print only two stars instead of six? What mistake was made
# with variable j?
# i = 1
# j = 1
# while i <= 3:
#     while j <= 2:
#         print('*', end='')
#         j += 1
#     i += 1
# Answer: j is never reset inside the outer loop. After the first iteration of i,
# j is already 3, so the inner while loop never runs again.
# Fix: move j = 1 inside the outer loop so it resets every time.
i = 1
while i <= 3:
    j = 1           # j needs to reset here inside the outer loop
    while j <= 2:
        print('*', end='')
        j += 1
    i += 1
print()


# 24. Which is the first integer whose square is strictly greater than 20?
# found = False
# x = 1
# while not found:
#     if x * x > 20:
#         found = True
#     else:
#         x += 1
# print(x)
# Answer: x = 5 because 5*5 = 25 which is greater than 20
found = False
x = 1
while not found:
    if x * x > 20:
        found = True
    else:
        x += 1
print(x)


# 25. If the user inputs 4, 7, -1, and 10 in sequence, is the -1 added to the total? What is
# the final printed total?
# total = 0
# user_input = 0
# while user_input != -1:
#     total += user_input
#     user_input = int(input('enter: '))
# print(total)
# Answer: Yes, -1 IS added to the total here because total += user_input runs
# before the check. But user_input starts at 0, so total = 0 + 4 + 7 + (-1) = 10
# The final printed total is 10
total = 0
user_input = 0
inputs = [4, 7, -1, 10]  # simulating user input
idx = 0
while user_input != -1:
    total += user_input
    user_input = inputs[idx]
    idx += 1
print(total)


# 26. How many times does the word loop print? What is the final value of x?
# x = 10
# while x < 5:
#     x += 1
#     print('loop')
# print(x)
# Answer: "loop" prints 0 times because x = 10 which is already not less than 5
# so the loop never runs. Final value of x is 10.
x = 10
while x < 5:
    x += 1
    print('loop')
print(x)


# 27. In many languages, an integer can act as a Boolean expression. At what point does
# x evaluate to False?
# x = 3
# while x:
#     print(x, end=' ')
#     x -= 1
# Answer: x evaluates to False when x becomes 0
x = 3
while x:
    print(x, end=' ')
    x -= 1
print()


# 28. What famous mathematical number sequence is generated by this loop's variable
# updating logic?
# a, b = 0, 1
# while a < 10:
#     print(a, end=' ')
#     a, b = b, a + b
# Answer: The Fibonacci sequence
a, b = 0, 1
while a < 10:
    print(a, end=' ')
    a, b = b, a + b
print()


# 29. Write a Python function that accepts a string and counts the number of upper and
# lower case letters.
# sample string : 'The quick Brow Fox'
# expected output :
# No. of upper case characters : 3
# No. of lower case characters : 12
def count_case(s):
    upper = 0
    lower = 0
    i = 0
    while i < len(s):
        if s[i].isupper():
            upper += 1
        elif s[i].islower():
            lower += 1
        i += 1
    print("No. of upper case characters :", upper)
    print("No. of lower case characters :", lower)

count_case("The quick Brow Fox")


# 30. Write a program that displays the following menu repeatedly until the user
# chooses to exit:
# 1. Add two numbers
# 2. Subtract two numbers
# 3. Multiply two numbers
# 4. Exit
while True:
    print("\n1. Add two numbers")
    print("2. Subtract two numbers")
    print("3. Multiply two numbers")
    print("4. Exit")
    choice = int(input("Choose an option: "))
    if choice == 4:
        print("Goodbye!")
        break
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    if choice == 1:
        print("Result:", a + b)
    elif choice == 2:
        print("Result:", a - b)
    elif choice == 3:
        print("Result:", a * b)
    else:
        print("Invalid option.")


# 31. Write a program that repeatedly asks the user to enter numbers until they enter
# 0. Count how many positive and negative numbers were entered exclude 0.
positive = 0
negative = 0
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    elif num > 0:
        positive += 1
    else:
        negative += 1
print("Positive numbers:", positive)
print("Negative numbers:", negative)


# 32. Write a program that takes two numbers start and end and prints all prime
# numbers between them using while loops.
def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

start = int(input("Enter start: "))
end = int(input("Enter end: "))
n = start
while n <= end:
    if is_prime(n):
        print(n, end=" ")
    n += 1
print()


# 33. Write a program to find the numbers which are below 20 in the list.
# numbers = [12, 40, 21, 31, 10, 7, 5]
numbers = [12, 40, 21, 31, 10, 7, 5]
i = 0
while i < len(numbers):
    if numbers[i] < 20:
        print(numbers[i], end=" ")
    i += 1
print()


# 34. Write a program to replace all numbers greater than 50 with 0 in the list and print
# the updated list.
# numbers = [45, 60, 12, 75, 30, 55, 8, 90]
numbers = [45, 60, 12, 75, 30, 55, 8, 90]
i = 0
while i < len(numbers):
    if numbers[i] > 50:
        numbers[i] = 0
    i += 1
print("Updated list:", numbers)


# 35. Write a program to count how many numbers are divisible by both 3 and 5 in the
# list.
# numbers = [15, 25, 30, 45, 60, 12, 90, 7]
numbers = [15, 25, 30, 45, 60, 12, 90, 7]
count = 0
i = 0
while i < len(numbers):
    if numbers[i] % 3 == 0 and numbers[i] % 5 == 0:
        count += 1
    i += 1
print("Count:", count)


# 36. Write a program to check whether the list is in ascending order or not using a
# while loop. Print sorted or not sorted numbers = [10, 15, 25, 30, 45]
numbers = [10, 15, 25, 30, 45]
i = 0
is_sorted = True
while i < len(numbers) - 1:
    if numbers[i] > numbers[i + 1]:
        is_sorted = False
        break
    i += 1
if is_sorted:
    print("Sorted")
else:
    print("Not sorted")


# 37. Print alphabet series a to z.
ch = ord('a')
while ch <= ord('z'):
    print(chr(ch), end=" ")
    ch += 1
print()


# 38. Write a program that iterates through the list of chapter page counts [45, 30, 50,
# 40] and starting the count at 1 to print a message for each chapter in the format:
# Chapter [Number] has [Pages] pages
chapters = [45, 30, 50, 40]
i = 0
while i < len(chapters):
    print(f"Chapter {i + 1} has {chapters[i]} pages")
    i += 1


# 39. You have two lists of numbers, and you need to find out which numbers appear
# in both lists.
# Given two lists of numbers [1,2,3,4,5] and [3,4,5,6,7]
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common = []
i = 0
while i < len(list1):
    j = 0
    while j < len(list2):
        if list1[i] == list2[j]:
            common.append(list1[i])
        j += 1
    i += 1
print("Common numbers:", common)


# 40. Print multiplication table of 2,4,6,7,8
tables = [2, 4, 6, 7, 8]
t = 0
while t < len(tables):
    num = tables[t]
    print(f"\nTable of {num}:")
    i = 1
    while i <= 10:
        print(f"{num} x {i} = {num * i}")
        i += 1
    t += 1


# 41. Write a program to check whether the list contains any duplicate numbers or not
# using a while loop. If the list has any duplicate, print has Duplicates, otherwise
# print no duplicates.
numbers = [1, 2, 3, 4, 2, 5]
seen = []
has_duplicate = False
i = 0
while i < len(numbers):
    if numbers[i] in seen:
        has_duplicate = True
        break
    seen.append(numbers[i])
    i += 1
if has_duplicate:
    print("Has Duplicates")
else:
    print("No Duplicates")