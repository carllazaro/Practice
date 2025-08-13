# Get each digit from a number in the reverse order.
# For example, If the given integer number is 7536, the output 
# shall be “6 3 5 7“, with a space separating the digits.

while True:
    number = int(input("Enter a 4 digit number: "))
    number = str(number)
    if len(number) == 4:
        print(number[::-1])
        break
    else:
        print("only 4 digit!")
        continue