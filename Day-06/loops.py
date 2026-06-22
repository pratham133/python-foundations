# Program 1 (Print Hello)

# Print Hello 5 times
for i in range(5):
    print("Hello")


# Program 2 (Print Numbers)

# Print numbers from 1 to 5
for i in range(1,6):
    print(i)


# Program 3 (Print Name Multiple Times)

# Get name input
name = input("Enter your name: ")

# Print name 3 times
for i in range(3):
    print(name)


# Program 4 (Multiplication Table)

# Get number input
number = int(input("Enter the number: "))

# Print table
for i in range(1,11):
    print(number, "x", i, "=", number * i)


# Program 5 (Sum of Numbers)

# Store total
total = 0

# Add numbers from 1 to 5
for i in range(1,6):
    total = total + i

# Show result
print("Total:", total)


# Program 6 (Sum of User Numbers)

# Get limit input
number = int(input("Enter the number: "))

# Store total
total = 0

# Add numbers
for i in range(1, number + 1):
    total += i

# Show result
print("Total:", total)


# Final program (Even Numbers Printer)

# Get number input
num = int(input("Enter the number: "))

# Print even numbers
for i in range(1, num + 1):

    # Check even number
    if i % 2 == 0:
        print(i)
