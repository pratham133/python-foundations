# Program 1 (Function with One Parameter)

def greet(name):
    print(f"Hello! {name}")

greet("Pratham")
greet("Python")


# Program 2 (Function with Two Parameter)

def add_numbers(a, b):
    print(f"Sum: {a + b}")

add_numbers(10, 5)
add_numbers(8, 30)


# Program 3 (Function that Returns a Value)

def add_numbers(a, b):
    return a + b

result = add_numbers(10, 20)
print(f"Sum: {result}")


# Program 4 (Print vs Return)

def show_sum(a, b): 
    print(a + b)

def give_sum(a, b):
    return a + b

show_sum(10, 20)

result = give_sum(10, 20)
print(result)


# Program 5 (Multiplication Function)

def multiply(a, b):
    return a * b 

result = multiply(6, 7)
print(f"Multiplication: {result}")


# Program 6 (Function with String Return)

def full_name(first_name, last_name):
    return first_name + " " + last_name

name = full_name("Pratham", "Pasi")
print(f"Full name: {name}")

# Quick Challenge
def make_city(city):
    return "I live in " + city
print(make_city("Mumbai")) 


# Program 7 (Function Practice)

def calculate_square(number):
    return number ** 2

def greet_user(name):
    return f"Hello, {name}"

def add_number(a, b):
    return a + b

number = int(input("Enter the number for square: "))
for_sum_input_1 = int(input("Enter the first number: "))
for_sum_input_2 = int(input("Enter the second number: "))

print(greet_user("Pratham"))
print(f"Square of {number}: {calculate_square(number)}")
print(f"Sum of {for_sum_input_1} and {for_sum_input_2}: {add_number(for_sum_input_1, for_sum_input_2)}")