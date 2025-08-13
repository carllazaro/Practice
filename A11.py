# Calculate income tax for the given income by adhering to the rules below

# Taxable Income	    Rate (in %)
# First $10,000	        0
# Next $10,000	        10
# The remaining	        20

# Expected Output:

# For example, suppose the income is 45000, and the income tax payable is
# 10000*0% + 10000*10%  + 25000*20% = $6000
def calculate_tax(income):
    tax = 0

    if income <= 10000:
        tax = 0
    elif income <= 20000:
        tax = (income - 10000) * .10
    else:
        tax = (10000 * 0) + (10000 * 0.10) + ((income - 20000) * 0.20)
    return tax

income = float(input("Enter income: "))
tax_payable = int(calculate_tax(income))
print(f"Tax payable is : {tax_payable}")


#STILL IMPROVING WITH THIS PRACTICES!!!