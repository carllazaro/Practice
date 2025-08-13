#Write a Python code to accept a string from the user and 
# display characters present at an even index number.

#For example, str = "PYnative". so your code should display ‘P’, ‘n’, ‘t’, ‘v’.

string_input = input("Type a string: ")
print(f"Original String is {string_input}")
print("Printing only even chars")

even = len(string_input)

for i in range(even):
    if i % 2 == 0:
        print(i, string_input[i])
