# ==========================================
# Program 1 (Without Exception Handling)
# ==========================================

number = int(input("Enter a number: "))

print(f"You entered: {number}")


# ==========================================
# Program 2 (Handling ValueError)
# ==========================================

try:
    number = int(input("Enter a number: "))
    print(f"You entered: {number}")

except ValueError:
    print("Invalid input! Please enter a valid integer/number.")


# ==========================================
# Program 3 (Handling Multiple Exceptions)
# ==========================================

try:
    number = int(input("Enter a number: "))
    result = 10/number

    print(f"Result: {result}")

except ValueError:
    print("Invalid input!, Enter a valid integer/number.")

except ZeroDivisionError:
    print("You cannot divide by zero.")


# ==========================================
# Program 4 (Handling Different Exceptions)
# ==========================================

try:
    numbers = [10, 20, 30]

    index = int(input("\nEnter index: "))

    print(numbers[index])

except ValueError:
    print("Please enter a valid integer.")

except IndexError:
    print("Index out of range.")


# ==========================================
# Program 5 (Generic Exception)
# ==========================================

try:
    number = int(input("Enter a number: "))
    result = 100 // number

    print(f"Result: {result}")

except Exception as error:
    print(f"An error occurred: {error}")


# ==========================================
# Program 6 (Specific vs Generic Exception)
# ==========================================

try:
    number = int(input("\nEnter a number: "))
    result = 100 / number

    print(f"Result: {result}")

except ValueError:
    print("Invalid input! Only integer/number is allowed.")

except ZeroDivisionError:
    print("You cannot divide by zero(0)")

except Exception as error:
    print(f"💀 Error occurred: {error}")


# =============================================
# Program 7 (Multiple Exceptions in One Block)
# =============================================

try:
    number = int(input("Enter a number: "))
    result= 500 // number

    print(f"Result: {result}")

except(ValueError, ZeroDivisionError):
    print("Invalid input! Enter a non-zero integer.")


# ==========================================
# Program 8 (Using else)
# ==========================================

try:
    number = int(input("Enter a number: "))
   
except ValueError:
    print("Invalid input!")

else:
    print(f"You entered: {number}")


# ==========================================
# Program 9 (Using finally)
# ==========================================

try: 
    number = int(input("Enter a number: "))

except ValueError:
    print("Invalid input!")

else:
    print(f"You entered: {number}")

finally:
    print("Program execution completed.")


# ==========================================
# Program 10 (Using raise)
# ==========================================

age = int(input("\nEnter your age: "))

if age < 18:
    raise ValueError("You must be at least 18 years old.")

print("Your are eligible.")


# ==========================================
# Program 11 (Custom Exception)
# ==========================================

class InvalidAgeError(Exception):
    pass

age = int(input("\nEnter your age: "))

if age < 18:
    raise InvalidAgeError("You must be at least 18 years old.")

print("You are eligible.")


