num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Enter 1 for addition / Enter 2 for subtraction / Enter 3 for multiplication / Enter 4 for division")

entered_number = int(input("Enter your choice from 1 to 4: "))

if entered_number == 1:
    print(num1 + num2)
elif entered_number == 2:
    print(num1 - num2)
elif entered_number == 3:
    print(num1 * num2)  
elif entered_number == 4:
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid input. Please enter a number between 1 and 4.")  