# Check Palindrome Number
# Write a Python code to check if the given number is a palindrome. A palindrome number reads the same forwards and backward. For example, 545 is a palindrome number.

# Expected Output:

# original number 121
# Yes. given number is palindrome number

# original number 125
# No. given number is not palindrome number

number = int(input("Enter a number: "))
number = str(number)

if number[0] == number[-1]:
    print("original number", number)
    print("Yes. Given number is a palindrome number")
else:
    print("original number", number)
    print("No. Given number is a palindrome number")
