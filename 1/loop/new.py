from numpy import negative


students= {
    "ram":76,
    "sita":44,
    "hari":91,
    "gita":33
}
for i in students:
    print(i)
for i in students.keys():
    print(i)
for i in students.values():
    print(i)
for i in students.items():
    print(i)
    
    
#to print the student name whose marks is greater than 44
for i in students:
    if students[i]>44:
        print(i)
        print(students[i])

#to print the student whose student name starts from "R" or "S"
for i in students:
    if i.startswith("r") or i.startswith("s"):
        print(i)
        print(students[i])
        
#to print the student whose student name starts from 'r' and marks is greater than 44
for i in students:
    if i.startswith("r") and students[i]>44:
        print(i)
        print(students[i])
        
# to print the list of items, quantity, price and total price of each item in the cart

cart={
    "rice":(2,140),
    "milk":(3,50),
    "bread":(4, 35)
}
for i in cart:
    print(i)
    quantity=cart[i][0]
    price=cart[i][1]
    total_price=quantity*price
    print(f"quantity: {quantity}, price: {price}, total price: {total_price}")
    
#
for i in cart:
     print(f"{i}: quantity: {cart[i][0]}, price: {cart[i][1]}, total price: {cart[i][0]*cart[i][1]}")
total=0
for i in cart:
    total+=cart[i][0]*cart[i][1]
print("total price of the cart is:", total)


total_price=0
for i,(j,k) in cart.items():
    print(f"{i}: quantity: {j}, price: {k}, total price: {j*k}")
total=0
for i,(j,k) in cart.items():
    total+=j*k
print("total price of the cart is:", total)

#to store file after removing .exe file
file_name=["copy.py", "photo.jpg","xyz.exe"]
for i in file_name:
    if i.endswith(".exe"):
        removed_file=i
        file_name.remove(i)
print("file after removing .exe file:", file_name)

add_file=input("enter the file name to add:")
if add_file.endswith(".exe"):
    print("exe file cannot be added")
else:
    file_name.append(add_file)
print("file after adding the file:", file_name)


# to move items to a particular container

item=[1,2,3,"a", "b", "c",2+3j,11.3 ]

integer=[]
string=[]
complex=[]
float=[]
for i in item:
    if type(i)==int:
        integer.append(i)
    elif type(i)==str:
        string.append(i)
    elif type(i)==complex:
        complex.append(i)
    elif type(i)==float:
        float.append(i)
    else:
        print("invalid item")
print("integer:", integer)
print("string:", string)
print("complex:", complex)
print("float:", float)

# to fidn how many times a particular item is present in the list
item=[1,2,3,"a", "b", "c",2+3j,11.3, 1, "a", 2+3j,"ram", "shyam", "hari", "gita", "ram", "shyam", "hari", "gita"]
item_count={}
for i in item:
    if i in item_count:
        item_count[i]+=1
    else:
        item_count[i]=1
print("item count:", item_count)


#to find the number of time a particular item is present in the list using get method
item={1,2,3,"a", "b", "c",2+3j,11.3, 1, "a", 2+3j,"ram", "shyam", "hari", "gita", "ram", "shyam", "hari", "gita"}
item_count={}
for i in item:
    item_count[i]=item_count.get(i,0)+1
print("item count:", item_count)

##o print theonly items which are repeated more than 1 times in the list.
item=[1,2,3,"a", "b", "c",2+3j,11.3, 1, "a", 2+3j,"ram", "shyam", "hari", "gita", "ram", "shyam", "hari", "gita"]
item_count={}
for i in item:
    item_count[i]=item_count.get(i,0)+1
print(item_count)

for i in item_count:
    if item_count[i]>1:
        print(i)
else:
    print("no item is repeated more than 1 time")
    
    
# to separate even and odd numbers form the list and print them in separate lists
cart=[1,2,3,-11,13,14,-20]
"""
expected output:
[1,3,13,10,12,24]
[2,14]
[-11,-20]
"""
even=[]
odd=[]
for i in cart:
    if i < 0:
        negative.append(i)
    elif i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("even numbers:", even)
print("odd numbers:", odd)
print("negative numbers:", negative)

