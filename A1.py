#Given two integer numbers, write a Python program to return their product only if 
# the product is equal to or lower than 1000. Otherwise, return their sum.

number1 = int(input("number1 = "))
number2 = int(input("number2 = "))

product = number1 * number2
sum_ = number1 + number2

if product == 1000 or product < 1000:
    print(f"The result is {product}")
else:
    print(f"The result is {sum_}")
