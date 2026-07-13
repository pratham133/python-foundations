# ==========================================
# Program 1 (Returning a List)
# ==========================================

def get_number():

    numbers = [1, 2, 3, 4, 5]

    return numbers

result = get_number()

print(result)


# ==========================================
# Program 2 (First Generator)
# ==========================================

def get_numbers():

    yield 1 
    yield 2
    yield 3
    yield 4
    yield 5

result = get_numbers()

print(result)


# ==========================================
# Program 3 (Using next() with a Generator)
# ==========================================

def get_numbers():

    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

generator = get_numbers()

print(next(generator))
print(next(generator))
print(next(generator))


# ============================================
# Program 4 (Using for Loop with a Generator)
# ============================================

def get_numbers():

    yield 10
    yield 20
    yield 30
    yield 40

generator = get_numbers()

for number in generator:
    print(number)


# ==========================================
# Program 5 (Generator vs List)
# ==========================================

def get_list():

    return [1, 2, 3, 4, 5]

def get_generator():

    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

numbers_list = get_list()
numbers_generator = get_generator()

print(numbers_list)
print(get_generator)


# ==========================================
# Program 6 (Infinite Generator)
# ==========================================

def infinite_numbers():

    number = 1

    while True:

        yield number

        number += 1

generator = infinite_numbers()

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
