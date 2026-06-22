# Program 1 (First Function)

from numpy import number


def greet():
    print("Hello, Pratham!")

greet()


# Prgoram 2 (Call Function Multiple Times)

def greet():
    print("Hello!")

greet()
greet()
greet()


# Program 3 (Function to Add Numbers)

def add_numbers():
    num1 = 10
    num2 = 20
    total = num1 + num2
    print("Total:", total)

add_numbers()


# Program 4 (Function to Find Square)

def find_square():
    number = 6
    square = number ** 2
    print("Square:", square)

find_square()


# Program 5 (Function with User Input)

def check_even_odd():
    number = int(input("Enter a number: "))

    if number % 2 == 0:
        print("Even number")
    else: 
        print("Odd number")

check_even_odd()


# Program 6 (Function to Add Two Numbers)

def add_two_numbers():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    total = num1 + num2 
    print("Total:", total)

add_two_numbers()


# Program 7 (Function to Print Table)

def print_table():
    number = int(input("Enter number: "))

    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

print_table()


# Program 8 (Fnction to check  NUmber Type)

def check_number():
    number = int(input("Enter a number: "))

    if number > 0:
        print("Positive number")
    elif number < 0: 
        print("Negative number")
    else:
        print("Zero")

check_number()

    