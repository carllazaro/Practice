#Write Python code to iterate through the first 10 numbers and, 
# in each iteration, print the sum of the current and previous number.

range_ = int(input("Range: "))
print(f"Printing current and previous number sum in a range ({range_})")
previous_num = 0

for i in range(range_):
    print(f"Current Number {i} Previous Number {previous_num} Sum: {i + previous_num}")
    previous_num = i
    