# Merge two lists using the following condition

# Given two lists of numbers, write Python code to create a new list containing 
# odd numbers from the first list and even numbers from the second list.

# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 60, 75, 90]
# result list: [25, 35, 40, 60, 90]

list1 = []
list2 = []
merged_list = []

for i in range(5):
    list1_input = int(input("Enter a number for list 1: "))
    list1.append(list1_input)

for j in range(5):
    list2_input = int(input("Enter a number for list 2: "))
    list2.append(list2_input)
print(list1, list2)

for check_list1 in list1:
    if check_list1 % 2 == 1:
        merged_list.append(check_list1)

for check_list2 in list2:
    if check_list2 % 2 == 0:
        merged_list.append(check_list2)

print(merged_list)
