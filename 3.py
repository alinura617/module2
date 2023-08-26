#Alinura Sultanova
#07/10/2023
# A program that asks the user for two numbers and gives the user the possibility to choose
# between computing the sum and computing the product

# Ask the user for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Display menu options
print("Select an operation:")
print("1. Compute the sum")
print("2. Compute the product")

# Get user's choice
choice = int(input("Enter your choice (1 or 2): "))

# Perform the chosen operation and display the result
if choice == 1:
    result = num1 + num2
    print("The sum is:", result)
elif choice == 2:
    result = num1 * num2
    print("The product is:", result)
else:
    print("Invalid choice")

#Finish