# # Get an int value of base raises to the power of exponent
# # Write a function called exponent(base, exp) that returns 
# # an int value of base raises to the power of exp.

# base = 2
# exponent = 5

# 2 raises to the power of 5: 32 i.e. (2 *2 * 2 *2 *2 = 32)

base = int(input("base = "))
exponent_ = int(input("exponent = "))
exp = pow(base, exponent_)
print(f"{base} raises to the power of {exponent_}: {exp} | {base}", end = " ")
for i in range(4):
    print(f"*{base}", end = " ")
print(f" = {exp}")