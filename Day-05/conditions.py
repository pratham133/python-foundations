# Program 1 (Voting Eligibility)

# Get age input
age = int(input("Enter your age: "))

# Check eligibility
if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")


# Program 2 (Pass or Fail)

# Get marks input
marks = int(input("Enter your marks: "))

# Check result
if marks >= 35:
    print("You passed")
else:
    print("You failed")

# Program 3 (Grade Calculator)

# Get marks input
marks = int(input("Enter your marks: "))

# Check grade
if marks >= 90:
    print("Excellent")
elif marks >= 75:
    print("Good")
elif marks >= 35:
    print("Pass")
else:
    print("Fail")


# Program 4 (BMI Calculator)

# Get height and weight
weight = float(input("Enter your weight (kg): "))
height_cm = float(input("Enter your height (cm): "))

# Convert cm to meter
height_m = height_cm / 100

# Calculate BMI
bmi = weight / (height_m ** 2)

# Check BMI category
if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal weight")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")


# Program 5 (Even or Odd Checker)

# Get number input
num = int(input("Enter the number: "))

# Check even or odd
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# Final program (Number Checker)

# Get number input
number = int(input("Enter the number: "))

# Check positive, negative, or zero
if number > 0:
    print("Positive")

elif number < 0:
    print("Negative")

else:
    print("Zero")

# Check even or odd
if number % 2 == 0:
    print("Even number")

else:
    print("Odd number")
