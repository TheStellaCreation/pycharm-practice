# Python program for
# Creation of Arrays

import numpy as np

# creating a rank 1 array
arr = np.array([1, 2, 3])
print("Array with rank 1: \n", arr)

# creating a rank 2 array
arr = np.array([[1, 2, 3], [4, 5, 6]])
print("Array with rank 2: \n", arr)

# creating an array from tuple
arr = np.array((1, 3, 2))
print("\nArray created using "
      "passed tuple:\n", arr)

# Python program to demonstrate
# indexing in numpy array
import numpy as np

# Initial Array
arr = np.array([[-1, 2, 0, 4],
                [4, -0.5, 6, 0],
                [2.6, 0, 7, 8],
                [3, -7, 4, 2.0]])
print("Initial Array: \n", arr)


# Printing a range of Array
# with the use of slicing method
# [start : end] select from start to end
sliced_arr = arr[:2, ::2]
print("Array with first 2 rows and"
      " alternate columns(0 and 2):\n", sliced_arr)

# Printing elements at
# specific Indices
Index_arr = arr[[1, 1, 0, 3],
                [3, 2, 1, 0]]
print("\nElements at indices (1, 3), "
      "(1, 2), (0, 1), (3, 0):\n", Index_arr)

arr = np.array([1,2,3,4,5,6,7])
print("\n\none raw \n", arr)

sliced_arr = arr[:4]
print(sliced_arr)

# Python program to demonstrate
# basic operations on single array
import numpy as np

# Defining Array 1
a = np.array([[1, 2],
              [3, 4]])

# Defining Array 2
b = np.array([[4, 3],
              [2, 1]])

# Adding 1 to every element
print("\n\nAdding 1 to every element:\n", a + 1)

# Subtracting 2 from each element
print("\nSubtracting 2 from each element:\n", b - 2)

# sum of array elements
# Performing Unary operations
print("\nSum of all array "
      "elements: ", a.sum())

# Adding two arrays
# Performing Binary operations
print("\nArray sum:\n", a + b)

print("\narray multi\n", a*b)
