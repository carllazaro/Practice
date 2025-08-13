# Given list is  [10, 20, 33, 46, 55]
# Divisible by 5
# 10
# 20
# 55

given_list = []

while True:
    if len(given_list) == 5:
        break
    else:
        given_list_input = int(input("Enter a number: "))
        given_list.append(given_list_input)
        continue

for div in given_list:
    if div % 5 == 0:
        print(div)