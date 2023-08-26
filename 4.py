#Alinura Sultanova
#07/10/2023
#A program that calculates the users BMI (Body Mass Index). You will need to collect their
#height and weight. What would you name these input variables? What would you name the
#output variable?

# Collect user's height and weight
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

# Calculate BMI
bmi = weight / (height ** 2)

# Display the calculated BMI
print("Your BMI is:", bmi)

#Finish