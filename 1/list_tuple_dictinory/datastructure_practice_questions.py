# 1. Write a program to remove the item present at index 4 and add it to the 2nd position and at the end of the list.
# items = [3,5,7,9,11,13]
items = [3,5,7,9,11,13]
value = items.pop(4)
items.insert(1, value)
items.append(value)
print(items)

# 2. Given two sets

# first_set = {23, 42, 65, 57, 78, 83, 29}
# second_set = {57, 83, 29, 67, 73, 43, 48}

# Write a code to identify their intersection. Remove these common elements specifically from the first_set.
first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

common = first_set.intersection(second_set)
first_set -= common
print("Common elements:", common)
print("Updated first_set:", first_set)

# 3. Write a program to determine if first_set is a subset or superset of second_set. If a relationship is found, delete all elements from the set that is identified as the subset.

# first_set = {27, 43, 34}
# second_set = {34, 93, 22, 27, 43, 53, 48}
first_set = {27, 43, 34}
second_set = {34, 93, 22, 27, 43, 53, 48}

if first_set.issubset(second_set):
    print("first_set is subset of second_set")
    first_set.clear()

elif first_set.issuperset(second_set):
    print("first_set is superset of second_set")
    first_set.clear()

else:
    print("No subset/superset relationship")

print(first_set)

# 4. Given a dictionary month containing names and numerical values, write a script to extract all values and store them in a list. Ensure the final list contains no duplicate values.

# month = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53,
#          'july': 54, 'Aug': 44, 'Sept': 54}
month = {
    'jan': 47, 'feb': 52, 'march': 47, 'April': 44,
    'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54
}

values_list = list(set(month.values()))

print(values_list)

# 5. Write a code to remove duplicates from a list and create a tuple and find the minimum and maximum number

# sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
sample_list = [87, 45, 41, 65, 94, 41, 99, 94]

unique_list = list(set(sample_list))
result_tuple = tuple(unique_list)

print("Tuple:", result_tuple)
print("Min:", min(result_tuple))
print("Max:", max(result_tuple))

# 6. Write a Python program that defines two sets:

# club_A = {"ram", "hari", "shyam"}
# club_B = {"ram", "gita", "hari"}
# The program should check whether the two clubs have any members in common.
# If they do, print the following members exist in both groups and if they have no common members, print no overlapping members found between groups

club_A = {"ram", "hari", "shyam"}
club_B = {"ram", "gita", "hari"}
common = club_A.intersection(club_B)
if common:
    print("Following members exist in both groups:", common)
else:
    print("No overlapping members found between groups")
    

# 7. Define required_tasks and completed_tasks.

# required_tasks = {"Email", "Report", "Meeting"}
# completed_tasks = {"Email", "Report"}

# Write a program to verify if all required_tasks have been finished by checking if required_tasks is a subset of completed_tasks. Print all tasks done or some tasks pending accordingly
required_tasks = {"Email", "Report", "Meeting"}
completed_tasks = {"Email", "Report"}
if required_tasks.issubset(completed_tasks):
    print("All tasks done")
else:
    print("Some tasks pending")
    pending_tasks = required_tasks - completed_tasks
    print("Pending tasks:", pending_tasks)
    
    