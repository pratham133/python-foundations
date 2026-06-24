# Program 1 (Basic try and except) 

try: 
    number = int(input("Enter a number: "))
    print(f"You entered: {number}")
except ValueError:
    print("Invalid input! Please enter a valid number.")


# Program 2 (Handle Division by Zero)

try: 
    number = int(input("Enter a number: "))
    result = 100 / number
    print(f"Result: {result}")
except ZeroDivisionError:
    print("You cannot divide by zero!") 


# Program 3 (Handle Multiple Exceptions)

try: 
    number = int(input("Enter a number: "))
    result = 100 / number
    print(f"Result: {result}")

except ValueError:
    print("Ivalid input! Please enter a valid number.")

except ZeroDivisionError:
    print("You cannot divide by zero!")


# Program 4 (Using else)

try:
    number = int(input("Enter a number: "))
    result = 50 / number

except ValueError:
    print("Invalid input!")

except ZeroDivisionError:
    print("You cannot divide by zero.")

else:
    print(f"Result: {result}")
    print("Divison successful")


# Program 5 (Using finally)

try: 
    number = int(input("Enter a number: "))
    result = 100 / number

except ValueError:
    print("Invalid input!")

except ZeroDivisionError:
    print("You cannot divide by zero.")

finally:
    print("Program finished")


# Program 6 (Handle File not Found Error)

try:
    with open("missing.txt","r") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("File not found! Please check the file name.")  


# Program 7 (Safe Calculator)

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

except (ValueError, ZeroDivisionError):
    print("Invalid input! or You cannot divide by zero.")

else:
    print(f"Result: {result}")

finally:
    print("Calculator program ended.")
