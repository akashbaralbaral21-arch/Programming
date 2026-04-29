# '''Methods
# upper(), lower(), title(), capitalize(), swapcase()'''
# (1. A hospital system stores patient names in random case for example
# rahUl DahaL. Write a program to display the name in proper title format
# on the prescription.
patient_name=input("enter patient name: ")
print(patient_name.title())
# 2. A cybersecurity system requires all passwords to be checked in
# lowercase for consistency. Take a password input like ‘Pass@123’ and
# convert it for comparison.
password=input('enter a password: ')
if password == password.lower() and "@" in password and len(password) >=8:
    print("password is valid")
else:
    print('password is invalid')


# 3. A movie ticket booking system receives the movie name in lowercase
# ‘spider-man no way home’. Display it in title case on the ticket.
movie_name="spider-man no way home"
print(movie_name.title())

# 4. A school notice board program takes a heading input and displays it in
# ALL CAPS for attention. Take input ‘annual sports day’ and display it.

heading= input("enter a program")
print(heading.upper())


# 5. A fun CAPS-LOCK reversal tool takes the sentence ‘hELLO wORLD’ and
# swaps every letter's case. Write a program for this.
sentence="hELLO wORLD"
print(sentence.swapcase())

# Methods
# find(), index(), count(), startswith(), endswith()
# 6. A document editor wants to find the first position where the word ‘error’
# appears in a log message: ‘System error detected, error code 404’.

log_message="system error detected, error code 404"
print(log_message.find("error"))


# 7. An email validation system checks whether an entered email ends with
# ‘@gmail.com’. Write a program to validate it.

entered_email = "akshbaralbaral@gmail.com"
print(entered_email.endswith("@gmail.com"))

# 8. A spam filter counts how many times the word ‘free’ appears in a
# message: ‘Get free stuff, free gifts and free coupons now!’.

message="Get free stuff, free gifts and free coupons now!"
print(message.count("free"))

# 9. A URL checker verifies whether a website link starts with "https" for
# security. Write a program for this.
url = input("Enter a website URL: ")

if url.lower().startswith("https"):
    print("Secure website (HTTPS)")
else:
    print("Not secure (does not use HTTPS)")


# 10. A resume scanner checks whether the keyword ‘Python’ is present in
# a resume text. Use the in operator.

resume = input("Enter resume text: ")

if "Python" in resume:
    print("Keyword 'Python' found in resume")
else:
    print("Keyword 'Python' not found in resume")

# 11. A bank transaction log uses index() to find the exact position of the
# word ‘FAILED’ in the message ‘Transaction FAILED due to low balance’.
message = "Transaction FAILED due to low balance"

if "FAILED" in message:
    print(message.index("FAILED"))
else:
    print("FAILED not found in message")

# 12. A government office receives a file named ‘budget_report.pdf’. Write a
# Python program that checks whether the file is a PDF document or not
# using endswith() and directly print the result.
filename = "budget_report.pdf"

if filename.endswith(".pdf"):
    print("This is a PDF document")
else:
    print("This is not a PDF document")

# 13. A telecom registration system receives a phone number ‘+977-
# 9841123111’. Write a Python program that checks whether the phone
# number starts with the Nepal country code ‘+977’. Print the result
# directly.
phone_number = "+977-9841123111"

if phone_number.startswith("+977"):
    print("Valid Nepal number")
else:
    print("Invalid number")

# 14. A cybersecurity system receives a url ‘https://www.moha.gov.np/’.
# Write a Python program that checks whether the URL belongs to a
# government website, print the result directly.
url = "https://www.moha.gov.np/"

print(url.endswith(".gov.np"))

# Methods
# replace(), strip(), lstrip(), rstrip()
# 15. A customer feedback form receives input with extra spaces: ‘ Great
# service! ‘. Clean it before saving to the database.
feedback = "  Great   service!  "

cleaned_feedback = " ".join(feedback.split())

print(cleaned_feedback)


# 16. A chat application replaces all occurrences of a banned word ‘hate’
# with ‘****’ in the message "I hate this, hate it completely".
msg = "I hate this, hate it completely"
clean_message = msg.replace("hate", "****")
print(clean_message)

# 17. A file system receives filenames with leading slashes like
# ‘///student_records.pdf ‘. Remove the leading slashes.
filename = " ///student_records.pdf "

clean_filename = filename.strip().lstrip("/")
print(clean_filename)

# 18. A web scraper fetches product prices as ‘Price: $120.33 ‘ with trailing
# spaces. Clean the right side using rstrip() and remove symbols too.
price = "Price: $120.33   "

cleaned = price.rstrip().replace("Price: $", "")
print(cleaned)

# 19. A phone number formatter takes ‘+977 984-123-4567’ and removes
# all dashes - using replace() to store only digits format.
phone = "+977 984-123-4567"
cleaned = phone.replace("-", "")
print(cleaned)

# Methods
# split(), join()
# 20. A CSV file contains student data as ‘Aarav,22,Kathmandu,Computer
# Science’. Split it into individual fields and display each on a new line.
data = "Aarav,22,Kathmandu,Computer Science"

fields = data.split(",")
for field in fields:
    print(field)
    
# 21. A social media app stores hashtags as a ‘Python, Coding, Nepal, Tech’.
# Join them with # prefix to display as #Python #Coding #Nepal #Tech.
tags = "Python, Coding, Nepal, Tech"

tag_list = tags.split(", ")
result = "#" + " #".join(tag_list)
print(result)

# 22. A train ticket system receives passenger names separated by commas:
# ‘Ram, Shyam, Hari, Sita’. Split and count the total number of passengers.
passengers = "Ram, Shyam, Hari, Sita"

count = len(passengers.split(", "))
print("Total passengers:", count)

# 23. A sentence builder takes individual words [‘The’, ‘flight’, ‘departs’, ‘at’,
# ‘6AM’] and joins them with a space to form a proper sentence.
words = ['The', 'flight', 'departs', 'at', '6AM']

sentence = " ".join(words)

print(sentence)
# Methods
# isdigit(), isalpha(), isalnum(), isspace(), isupper(), islower()
# 24. A government form validation checks whether the entered age
# contains only digits. Take input ‘25’ or ‘25abc’ and validate it.
age = input("Enter age: ")
print(age.isdigit())

# 25. A username registration system checks that the username contains
# only letters and numbers, no special characters.
username = input("Enter username: ")
print(username.isalnum())

# 26. A name field validator in a school admission form checks that the
# student's name contains only alphabets (no digits).
name = input("Enter name: ")
print(name.isalpha())

# 27. A PIN verification system checks whether the user's PIN is all
# uppercase letters for a code like ‘ASDF’.
pin = input("Enter PIN: ")
print(pin.isupper())

# 28. A blank field detector in a form checks whether the user entered only
# spaces.
field = input("Enter value: ")
print(field.isspace())