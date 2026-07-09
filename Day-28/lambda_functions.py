# ==========================================
# Program 1 (Normal Function)
# ==========================================

def square(number):
    return number ** 2

result = square(5)

print(result)


# ==========================================
# Program 2 (Lambda Function)
# ==========================================

square = lambda number: number ** 2

result = square(8)

print(result)


# ==========================================
# Program 3 (Small challenge)
# ==========================================

cube = lambda number: number ** 3

print(cube(4))


# ==========================================
# Program 4 (Using map with Lambda)
# ==========================================

numbers = [1, 2, 3, 4, 5, 6]

squares = list(map(lambda number: number ** 2, numbers))

print(squares)


# ==========================================
# Program 5 (Using filter with Lambda)
# ==========================================

numbers = [10, 15, 20, 25, 30, 35]

even_numbers = list(filter(lambda number: number % 2 == 0, numbers))

print(even_numbers)


# ==========================================
# Program 6 (Using sorted() with Lambda)
# ==========================================

students = [

    {"name": "Pratham", "marks": 88},
    
    {"name": "Rahul", "marks": 72},

    {"name": "Anjali", "marks": 95},

    {"name": "Riya", "marks": 81}

]

sorted_students = sorted(
    students, 
    key=lambda student: student["marks"]
)

print(sorted_students)


# ==========================================
# Program 7 (Real World AI Example)
# ==========================================

predictions = [
    {"image": "cat.jpg", "confidence": 0.92},
    {"image": "dog.jpg", "confidence": 0.81},
    {"image": "bird.jpg", "confidence": 0.98}
]

sorted_predictions = sorted(
    predictions,
    key=lambda item: item["confidence"],
    reverse=True
)

print(sorted_predictions)

# Highest confidence prediction comes first.