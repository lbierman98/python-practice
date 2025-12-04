weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))

bmi = weight / (height * height )

print(f"Your BMI is {round(bmi, 2)}")
