# Solve these questions using for loop

# 1. Write a Python script using a for loop and the range() function to iterate through the numbers from 1 up to and including 5.

# Inside the loop, check if each number is even or odd, and then print the result in the format: "Number X is [even/odd]."

# Output

# Number 1 is odd.

# Number 2 is even.

# Number 3 is odd.

# Number 4 is even.

# Number 5 is odd.

for i in range(1,6):
    if i%2==0:
        print(f"Number {i} is even.")
    else:
        print(f"Number {i} is odd.")
        
    

# 2. Write a Python script that uses a for loop to calculate the sum of all elements in the given list.

# list = [10,20,30,40]

# Your script must:

# Initialize a variable to keep track of the running total.

# Iterate through the data list using a for loop.

# Inside the loop, print the value currently being added and the new running total.

# Finally, print the total sum after the loop finishes.

# Added 10. Running total is 10.

# Added 20. Running total is 30.

# Added 30. Running total is 60.

# Added 40. Running total is 100.

# ------------------------------

# Total Sum: 100
list = [10,20,30,40]
Total_sum=0
for i in list:
    Total_sum+=i
    print(f"Added {i}. Running total is {Total_sum}.")
    
print(f"Total sum: {Total_sum}")
          
# 3. Write a program that uses a for loop to iterate through the list student_names = ["Ram", "Hari", "Sita"] and prints a personalized message for each student in the format 'Hi [Name], your course approval is ready!'. Include the header ' --- Email Greetings Generated ---' before the loop.
student_names=["Ram", "Hari", "Sita"]
print("---Email Greetings Generated---")
for i in student_names:
    print(f"Hi {i}, your course approval is ready!.")

# 4. write a program that iterates through the list of chapter page counts [45, 30, 50, 40] and (starting the count at 1) to print a message for each chapter in the format: 'Chapter [Number] has [Pages] pages.'. Include the header '--- Book Chapter Summary ---'."
page_counts=[45, 30, 50, 40]
print("---Book Chapter Summary---")
for i in range(len(page_counts)):
    print(f"Chapter {i+1} has {page_counts[i]} pages.")
# 5. Write a Python script to calculate the product (multiplication) of all numeric elements in a given list. given list=[4,5,3,2]
list=[3,2,1,4,5]
product=1
for i in list:
    product*=i
    print(f"Product so far: {product}")

# 6. multiplication table of a given number. number= 11
for i in range(1,11):
    print(f"11 x {i} = {11*i}")

# 7. reverse a list given list = [3,2,1,4,5]

list = [3,2,1,4,5]
reversed_list=[]
for i in range(len(list)):
    reversed_list.append(list[len(list)-1-i])
    print(f"Reversed list so far: {reversed_list}")
    
# 8.  You have two lists of numbers, and you need to find out which numbers appear in both lists. 
# Given two lists of numbers [1,2,3,4,5] and [3,4,5,6,7] write a for  loop to find the common elements.
num1=[1,2,3,4,5]
num2=[3,4,5,6,7]
common_elements=[]
for i in num1:
    if i in num2:
        common_elements.append(i)
print(f"common elements: {common_elements}")

# 9. Given list is lst=[1,2,3,4] but print 1 and 4 only 

lst=[1,2,3,4]
list=[]
for i in lst:
    if i==1 or i==4:
        list.append(i)
        print(list)

# 10.  Write a that removes all vowels (a, e, i, o, u) from a string.
strintg = "Hello World"
vowels = "aeiouAEIOU"
result = ""
for char in strintg:
    if char not in vowels:
        result += char
        
print(f"String after removing vowels: {result}")
# 11.  Write a program that counts the total number of vowels and consonants in a given sentence, ignoring spaces and special characters. 

# given input: 

# 'Loops are Fun'

# expected Output:

# vowels: 5

# consonants: 7 

string="Loops are Fun"
vowels="aeiouAEIOU"
vowel_count=0
consonants_count=0
for char in string:
    if char in vowels:
        vowel_count+=1
    elif char.isalpha():
        consonants_count+=1
print(f"vowels: {vowel_count}\nconsonants: {consonants_count}")
        

# 12. Given list is [1,2,3,4,5] separate the elements into odd and even categories.
numbers = [1,2,3,4,5]
odd_numbers=[]
even_numbers=[]
for i in numbers:
    if i%2==0:
        even_numbers.append(i)
    else:
        odd_numbers.append(i)
print(f"odd numbers: {odd_numbers}\neven numbers: {even_numbers}")

# 13. Write a program to determine whether a given number is a prime number.
# Program to check if a number is prime
num = int(input("Enter a number: "))
if num <= 1:
    print(num, "is not a prime number")
else:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")

# 14. Given list is [1,2,3,4,"a","b"] append each elements datatypes to separate lists.
list=[1,2,3,4,"a","b"]
integers=[]
strings=[]
for i in list:
    if isinstance(i, int):
        integers.append(i)
    elif isinstance(i, str):
        strings.append(i)
print(f"Integers: {integers}\nStrings: {strings}")

# 15. Python program that accepts a string and calculate the number of digits and letters
string=input("Enter a string: ")
digits_count=0
letters_count=0
for i in string:
    if i.isdigit():
        digits_count+=1
    elif i.isalpha():
        letters_count+=1
print(f"Digits: {digits_count}\nLetters: {letters_count}")

# 16. Python program to check the validity of username and password input by users
username=input("Enter username:")
password=input("Enter password:")
if len(username)>=5 and len(password)>=8:
    print("Username and password are valid.")
else:
    print("Username must be at least 5 characters long and password must be at least 8 characters long.")
    
# 17. program to print the given number is odd or even
number=int(input("Enter a number:"))
if number%2==0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")
    
# 18. factorial of a given number
num=int(input("Enter a number:"))
factorial=1
for i in range(1, 11):
    factorial=num*i
    print(f" {num} * {i} = {factorial}  ")

# 19. Print multiplication table of  1,2,3,4,5,6,7,8 
list=[1,2,3,4,5,6,7,8]
for i in len(list):
    for j in range(1,11):
        print(f"{list[i]} x {j} = {list[i]*j}")

# 20. Given list is lst=[1,2,3,4] but print 1 and 2 only
lst=[1,2,3,4]
list=[]
for i in lst:
    if i==1 or i==2:
        list.append(i)
print(list)

# 21. Python program to calculate the sum of all the odd numbers within the given range.
number=int(input("Enter a number:"))
odd_sum=0
for i in range(1, number+1):
    if i%2 !=0:
        odd_sum+=i
print(f"Sum of odd numbers from 1 to {number} is: {odd_sum}")

# 22. Python program to calculate the sum of all the even numbers within the given range.
number=int(input("Enter a number:"))
even_sum=0
for i in range(1, number+1):
    if i%2==0:
        even_sum+=i
print(f"Sum of even numbers from 1 to {number} is: {even_sum}")
# 23. Python program to count the space of a given string
string=input("Enter a string:")
space_count=0
for i in string:
    if i.isspace():
        space_count+=1
print(f"Number of spaces in the string: {space_count}")
# 24. given list is [1,2,3,4] but expected output is [1,8,27,64]
list=[1,2,3,4]
cubed_list=[]
for i in list:
    cubed_list.append(i**3)
print(cubed_list)
    
# 25. reverse of a string a="programming". 
a="programming"
reversed_string=""
for i in range(len(a)):
    reversed_string+=a[len(a)-1-i]  
print(reversed_string)

# 26. Place a break statement in the for loop so that it prints from 0 to 7 only (including 7). Given range(50)
for i in range(50):
    if i<=7:
        print(i)
    else:
        break

# 27. Write a for loop that iterates through a string and prints every letter.
string="Hello World"
for i in string:
    print(i)
else:
    print("Done")
    

# 28. Write a for loop which print "Hello!, " plus each name in the list. i.e.: "Hello!, Ram". Hint a=["ram","shyam",1,2] expected output:  Hello!ram Hello!shyam
a=["ram","shyam",1,2]
for i in a:
    if isinstance(i, str):
        print(f"Hello!{i}")
    else:
        continue     
# 29. Using a for loop and .append() method append each item with a Dr. prefix to the lst. Hint a=["ram","shyam"] expected output:  ['Dr.ram', 'Dr.shyam','Dr.1','Dr.2']
a=["ram","shyam",1,2]
lst=[]
for i in a:
    lst.append(f"Dr.{i}")
print(lst)

# 30. Write a for loop which appends the square of each number to the new list.
numbers=[1,2,3,4,5]
squared_numbers=[]
for i in numbers:
    squared_numbers.append(i**2)
print(squared_numbers)

# 31. Write a for loop using an if statement, that appends each number to the new list if it's positive. given lst1=[111, 32, -9, -45, -17, 9, 85, -10]
lst1=[111, 32, -9, -45, -17, 9, 85, -10]
positive_numbers=[]
for i in lst1:
    if i>0:
        positive_numbers.append(i)
print(positive_numbers)

# 32. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6. given list=[0,1,2,3,4,5,6]
numbers=[0,1,2,3,4,5,6]
for i in numbers:
    if i==3 or i==6:
        continue
    else:
        print(i)


# 33. Write a for loop which appends the type of each element in the first list to the second list.
lst1=[111, 32, -9, -45, -17, 9, 85, -10]
types=[]
for i in lst1:
    types.append(type(i))
print(types)


# 34. Use else block to display a message “Done” after successful execution of for loop.
numbers=[1,2,3,4,5]
for i in numbers:
    print(i)
else:
    print("Done")

# 35. Write a for loop statement to print the following series: 

# 105 98 -------7
for i in range(105, 98-1, -7):
    print(i)

# 36. removal bad characters from the given string. Given bad_chars = [';', ':', '!', "*"], string = "py;th* o:n ! ;py * t*h:o !n".  Expected output = pythonpython
bad_chars = [';', ':', '!', "*"]
string = "py;th* o:n ! ;py * t*h:o !n"
for char in bad_chars:
    string = string.replace(char, "")
print(string)

# 37. Python program to count the number of even and odd numbers from a series of numbers.  
numbers=[1,2,3,4,5,6,7,8,9,10]
even_count=0
odd_count=0
for i in numbers:
    if i%2==0:
        even_count+=1
    else:
        odd_count+=1
print(f"Even numbers count: {even_count}\nOdd numbers count: {odd_count}")

# 38. Write a for loop to find the sum of all multiples of 3 or 5 below a given number range from 3 to 99.
total_sum=0
for i in range(3, 100):
    if i%3==0 or i%5==0:
        total_sum+=i
print(f"Sum of multiples of 3 or 5 below 100: {total_sum}")

# 39. Write a for loop to find the sum of even and odd numbers separately in a range from 1 to 100.
even_sum=0
odd_sum=0
for i in range(1, 101):
    if i%2==0:
        even_sum+=i
    else:
        odd_sum+=i
print(f"Sum of even numbers from 1 to 100: {even_sum}\nSum of odd numbers from 1 to 100: {odd_sum}")    

# 40. Given a list of numbers, use a loop to count how many times a specific number appears. 
# list1-[10,20,10,30,40,50]
#target_number=10
list1=[10,20,10,30,40,50]
target_number=10
count=0
for i in list1:
    if i==target_number:
        count+=1
print(f"Number {target_number} appears {count} times in the list.")



