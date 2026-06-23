# Program 1 (Function to Print Table)

def print_table(number):
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

user_input = int(input("Enter the number: "))
print_table(user_input)


# Program 2 (Function to find sum 1 to N)

def find_sum(n):
    total = 0

    for i in range(1, n+1):
        total += i
    
    print(f"Sum from 1 to {n} = {total}")

sum_input = int(input("Enter the Number: "))
find_sum(sum_input)


# Program 3 (Function to count vowels)

def count_vowels(text):
    count = 0

    for ch in text.lower():
        if ch in "aeiou":
            count += 1
    
    print(f"Number of Vowels: {count}")

word = input("Enter a word: ")
count_vowels(word)


# Program 4 (Function to print Even Numbers)

def print_even_number(start, end):
    for num in range(start, end + 1):
        if num % 2 == 0:
            print(num)

print_even_number(1, 10)


# Program 5 (Return Sum of Even NUmber)

def total_even_sum(start, end):
    total = 0

    for num in range(start, end + 1):
        if num % 2 == 0:
            total += num

    return total

result = total_even_sum(1, 10)
print(f"Sum of even numbers: {result}")


# Program 6 (Print Each Character)

def print_character(text):
    for ch in text:
        print(ch)

print_character("Python")


# # Program 6 (Loop + Function Practice)

def calculate_factorial(number):
    result = 1

    for i in range (1, number + 1):
        result *= i

    return result

def count_letter(text):
    count = 0

    for ch in text:
        count += 1

    return count

print(f"Factorial Of 5: {calculate_factorial(5)}")
print(f"Number of letters in Pratham: {count_letter('Pratham')}")