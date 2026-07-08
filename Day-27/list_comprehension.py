# ==========================================
# Program 1 (Traditional Method)
# ==========================================

numbers = [1, 2, 3, 4, 5]

squares = []

for number in numbers:
    squares.append(number ** 2)

print(squares)


# ==========================================
# Program 2 (Basic List Comprehension)
# ==========================================

numbers = [1, 2, 3, 4, 5]

squares = [number ** 2 for number in numbers]

print(squares)


# =============================================
# Program 3 (List Comprehension with Condition)
# =============================================

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = [number for number in numbers if number % 2 == 0]

print(even_numbers)


# ===============================================
# Program 4 (🤖 Real AI/Data Analytics Example)
# ===============================================

marks = [45, 87, 23, 91, 78, 34, 95]

passed_student = [mark for mark in marks if mark >= 60]

print(passed_student)