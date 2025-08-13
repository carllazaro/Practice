# Write a code to return True if the list’s first and last numbers are the same. 
# If the numbers are different, return False.

for_list_a = []
for_list_b = []

while True:
    if len(for_list_a) == 5:
        break
    else:
        input_for_list_a = int(input("Enter a number for list A : "))
        for_list_a.append(input_for_list_a)
        continue

while True:
    if len(for_list_b) == 5:
        break
    else:
        input_for_list_b = int(input("Enter a number for list B : "))
        for_list_b.append(input_for_list_b)
        continue
        
if for_list_a[0] == for_list_b[0] and for_list_a[4] == for_list_b[4]:
    print("True")
else:
    print("False")