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