# Slicing Tuples
# Slice below tuple to get elements from the 4th to the 7th position.

# Given:
# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# Expected Output:
# (4, 5, 6, 7)

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
new_set = ()
for i in range(3, 7):
    new_set += (numbers[i], )
print(numbers)
print(new_set)