# ==========================================
# Program 1 (Creating First NumPy Array)
# ==========================================

import numpy as np

arr1 = np.array([10,20,30,40,50])

print(type(arr1))


# ==================================================
# Program 2 (Comparing Python List and NumPy Array)
# ==================================================

import numpy as np

numbers_list = [10, 20, 30]

numbers_array = np.array([10, 20, 30])

print(type(numbers_list))

print(type(numbers_array))


# ==========================================
# Program 3 (Element-wise Addition)
# ==========================================

arr1 = np.array([10, 20, 30, 40, 50])

print(arr1 + 5)


# ==========================================
# Program 4 (Adding Two NumPy Arrays)
# ==========================================

import numpy as np

arr1 = np.array([10, 20, 30])

arr2 = np.array([1, 2, 3])

print(arr1 + arr2)


# ==========================================
# Program 5 (Subtracting Two NumPy Arrays)
# ==========================================

import numpy as np

arr1 = np.array([50, 40, 30])

arr2 = np.array([10, 20, 5])

print(arr1 - arr2)


# ==========================================
# Program 6 (Multiplication and Division)
# ==========================================

arr1 = np.array([10, 20, 30])

print(arr1 * 2)

print(arr1 / 2)


# ===============================================
# Program 7 (Finding the Shape of a NumPy Array)
# ===============================================

import numpy as np

arr1 = np.array([10, 20, 30, 40, 50])

print(arr1.shape)


# ==========================================
# Program 8 (Finding Number of Dimensions)
# ==========================================

import numpy as np

arr1 = np.array([10, 20, 30, 40, 50])

print(arr1.ndim)


# =============================================
# Program 9 (Finding Total Number of Elements)
# =============================================

import numpy as np

arr1 = np.array([10, 20, 30, 40, 50])

print(arr1.size)


# ==========================================
# Program 10 (Finding the Data Type)
# ==========================================

import numpy as np

arr1 = np.array([10, 20, 30, 40, 50])

print(arr1.dtype)


import numpy as np

arr = np.array([5, 10, 15, 20])

print(arr.shape)
print(arr.ndim)
print(arr.size)
print(arr.dtype)


# ==============================================
# Program 11 (Accessing Elements using Indexing)
# ==============================================

import numpy as np

arr1 = np.array([10, 20, 30, 40, 50])

print(arr1[0])
print(arr1[1])
print(arr1[2])


# ==========================================
# Program 12 (Negative Indexing)
# ==========================================

import numpy as np

arr1 = np.array([10, 20, 30, 40, 50])

print(arr1[-1])
print(arr1[-2])
print(arr1[-3])


# ==========================================
# Program 13 (Basic Array Slicing)
# ==========================================

import numpy as np

arr1 = np.array([10, 20, 30, 40, 50])

print(arr1[0:4])


# ==========================================
# Program 14 (Slice Shortcuts)
# ==========================================

import numpy as np

arr1 = np.array([10, 20, 30, 40, 50])

print(arr1[:])
print(arr1[:3])
print(arr1[2:])
print(arr1[-3:])
print(arr1[:-1])


# ==========================================
# Program 15 (Step Slicing)
# ==========================================

import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])

print(arr1[::2])
print(arr1[1::2])
print(arr1[::-1])


# ==========================================
# Program 16 (Creating a 2D NumPy Array)
# ==========================================

import numpy as np

students = np.array([
    [85, 90, 88],
    [78, 82, 80],
    [92, 95, 94]
])

print(students)


# ==============================================
# Program 17 (Accessing Elements in a 2D Array)
# ==============================================

import numpy as np

students = np.array([
    [85, 90, 88],
    [78, 82, 80],
    [92, 95, 94]
])

print(students[0][0])
print(students[1][2])
print(students[2][1])


# ==========================================
# Program 18 (Comma Indexing in NumPy)
# ==========================================

import numpy as np

students = np.array([
    [85, 90, 88],
    [78, 82, 80],
    [92, 95, 94]
])

print(students[0, 0])
print(students[1, 2])
print(students[2, 1])


# ==============================================
# Program 19 (Selecting Entire Rows and Columns)
# ==============================================

import numpy as np

students = np.array([
    [85, 90, 88],
    [78, 82, 80],
    [92, 95, 94]
])

print(students[0])
print(students[1])
print(students[:,1])
print(students[:,2])


# ============================================
# Program 20 (Selecting All Columns of a Row)
# ============================================

import numpy as np

students = np.array([
    [85, 90, 88],
    [78, 82, 80],
    [92, 95, 94]
])

print(students[0,:])
print(students[1,:])
print(students[2,:])
print(students[0:2, :])
print(students[:, 1:3])
print(students[0:2, 1:3])


# ==========================================
# Program 21 (Boolean Indexing)
# ==========================================

import numpy as np

marks = np.array([85, 90, 78, 95, 88, 72])

print(marks < 85)


# ===================================================
# Program 22 (Filtering Data using Boolean Indexing)
# ===================================================

import numpy as np

marks = np.array([85, 90, 78, 95, 88, 72])

high_marks = marks[marks > 85]

print(high_marks)
print(marks[marks < 85])

# ==========================================
# Program 23 (Reshaping a NumPy Array)
# ==========================================

import numpy as np

numbers = np.array([10, 20, 30, 40, 50, 60])

reshaped_array = numbers.reshape(2, 3)

print(reshaped_array)


# ==========================================
# Program 24 (Automatic Reshape using -1)
# ==========================================

import numpy as np

numbers = np.array([10, 20, 30, 40, 50, 60])

print(numbers.reshape(2, -1))

print(numbers.reshape(-1, 3))


# ==========================================
# Program 25 (Flattening a NumPy Array)
# ==========================================

import numpy as np

matrix = np.array([
    [10,20,30],
    [40,50,60]
])

flat = matrix.flatten()

print(matrix)


# ==========================================
# Program 26 (NumPy Statistical Functions)
# ==========================================

import numpy as np

marks = np.array([85, 90, 78, 95, 88])

print("Sum: ", np.sum(marks))
print("Mean", np.mean(marks))
print("Maximum: ", np.max(marks))
print("Minimum: ", np.min(marks))


numbers = np.array([10,20,30,40])

print(np.mean(numbers))


sales = np.array([25, 30, 28, 35, 32])

print(f"Sum: {np.sum(sales)}")
print(f"Average: {np.mean(sales)}")
print(f"Max: {np.max(sales)}")
print(f"Min: {np.min(sales)}")


# ==========================================
# Program 27 (NumPy Standard Deviation)
# ==========================================

import numpy as np

marks = np.array([85, 90, 78, 95, 88])

print(f"Mean: {np.mean(marks)}")
print(f"standard Deviation: {np.std(marks)}")


# ==========================================
# Program 28 (Generate Random Integers)
# ==========================================

import numpy as np

random_numbers = np.random.randint(1, 11, size=5)

print(random_numbers)


# ==========================================
# Program 29 (Random Decimal Numbers)
# ==========================================

import numpy as np

random_numbers = np.random.rand(5)

print(random_numbers)


# ==========================================
# Program 30 (Random Numbers Without Seed)
# ==========================================

import numpy as np

print(np.random.randint(1, 11, size=5))


# ==========================================
# Program 31 (Random Numbers With Seed)
# ==========================================

import numpy as np

np.random.seed(42)

print(np.random.randint(1, 11, size=5))


# ==========================================
# Program 32 (Concatenating NumPy Arrays)
# ==========================================

import numpy as np

arr1 = np.array([10, 20, 30])

arr2 = np.array([40, 50, 60])

result = np.concatenate((arr1, arr2))

print(result)


# ==========================================
# Program 33 (Horizontal Stack)
# ==========================================

import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

result = np.hstack((arr1, arr2))

print(result)


# ==========================================
# Program 34 (Vertical Stack)
# ==========================================

import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

result = np.vstack((arr1, arr2))

print(result)