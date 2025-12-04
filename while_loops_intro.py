num = int(input("Enter a number between 1 and 10: "))

while num < 1 or num > 10:
    print(f"Enter a number between 1 and 10: {num} is not a number between 1 and 10")
    num = int(input("Enter a number between 1 and 10: "))

print(f"your number is: {num}")
