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