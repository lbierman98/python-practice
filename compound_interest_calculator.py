Compound interest calculator

P = float(input("Enter a investment or loan amount: R"))
i = float(input("Enter the interest rate (%): "))
n = int(input("Enter the number of times compounded per year: "))
t = float(input("Enter the number of years: "))

while P <= 0:
    P = float(input("Enter a investment or loan amount: R"))
    if P <= 0:
        print("Principal amount cannot be less than or equal to zero.")
    else:
        break

while i <= 0:
    i = float(input("Enter the interest rate (%): "))
    if i <= 0:
        print("Interest rate cannot be less than or equal to zero.")
    else:
        break

while n <= 0:
    n = int(input("Enter the number of times compounded per year: "))
    if n <= 0:
        print("Compounding number cannot be less than or equal to zero.")
    else:
        break

while t <= 0:
    t = float(input("Enter the number of years: "))
    if t <= 0:
        print("Number of ears cannot be less than or equal to zero.")
    else:
        break

Final = P * pow((1 + ((i/100)/n)), (t * n))
print(f"The final amount that have/you need to bay back is R{Final:.2f}")
