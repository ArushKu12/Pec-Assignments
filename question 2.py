print("CALCULATE YOUR INCOME TAX")
name = input("enter your name:  ")
total_amount = int(input("enter your gross annual income:  "))
dependants = int(input("total dependants:  "))
standard_deduction = 10000
taxable_amount = (total_amount - standard_deduction - (3000*dependants))
income_tax = 0.2*taxable_amount
print(f"Total income tax to be paid by {name} is {income_tax}")