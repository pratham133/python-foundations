# ==========================================
# Program 1 (What is an Iterable?)
# ==========================================

numbers = [10, 20, 30, 40]

for number in numbers:
    print(number)


# ==========================================
# Program 2 (Creating an Iterator)
# ==========================================

numbers = [10, 20, 30, 40]

iterator = iter(numbers)

print(iterator)


# ==========================================
# Program 3 (Using next() with an Iterator)
# ==========================================

numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))


# ==========================================
# Program 4 (StopIteration Exception)
# ==========================================

# numbers = [1, 2, 3, 4]

# iterator = iter(numbers)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# print(next(iterator))


# ==========================================
# Program 5 (Manual For Loop Challenge)
# ==========================================

numbers = [100, 200, 300, 400]

iterator = iter(numbers)

while True:

    try:
        number = next(iterator)
        print(number)

    except StopIteration:
        print("Iteration completed.")
        break