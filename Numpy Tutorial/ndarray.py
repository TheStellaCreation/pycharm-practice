# Python program to demonstrate
# basic array characteristics
import numpy as np

# Creating array object
arr = np.array([[1, 2, 3],
                [4, 2, 5]])

# Printing type of arr object
print("Array is of type: ", type(arr))

# Printing array dimensions (axes)
print("No. of dimensions: ", arr.ndim)

# Printing shape of array
print("Shape of array: ", arr.shape)

# Printing size (total number of elements) of array
print("Size of array: ", arr.size)

# Printing type of elements in array
print("Array stores elements of type: ", arr.dtype)

# Python program to demonstrate
# array creation techniques
import numpy as np

# Creating array from list with type float
a = np.array([[1, 2, 4], [5, 8, 7]], dtype='float')
print("Array created using passed list:\n", a)

# Creating array from tuple
b = np.array((1, 3, 2))
print("\nArray created using passed tuple:\n", b)

# Creating a 3X4 array with all zeros
c = np.zeros((3, 4))
print("\nAn array initialized with all zeros:\n", c)

# Create a constant value array of complex type
d = np.full((3, 3), 6, dtype='complex')
print("\nAn array initialized with all 6s."
      "Array type is complex:\n", d)

# Python program to demonstrate
# indexing in numpy
import numpy as np

# An exemplar array
arr = np.array([[-1, 2, 0, 4],
                [4, -0.5, 6, 0],
                [2.6, 0, 7, 8],
                [3, -7, 4, 2.0]])

# Slicing array
temp = arr[:2, ::2]
print("Array with first 2 rows and alternate"
      "columns(0 and 2):\n", temp)

# Integer array indexing example
temp = arr[[0, 1, 2, 3], [3, 2, 1, 0]]
print("\nElements at indices (0, 3), (1, 2), (2, 1),"
      "(3, 0):\n", temp)

# boolean array indexing example
cond = arr > 0  # cond is a boolean array
temp = arr[cond]
print("\nElements greater than 0:\n", temp)

# Python program to demonstrate
# basic operations on single array
import numpy as np

a = np.array([1, 2, 5, 3])

# add 1 to every element
print("Adding 1 to every element:", a + 1)

# subtract 3 from each element
print("Subtracting 3 from each element:", a - 3)

# multiply each element by 10
print("Multiplying each element by 10:", a * 10)

# square each element
print("Squaring each element:", a ** 2)

# modify existing array
a *= 2
print("Doubled each element of original array:", a)

# transpose of array
a = np.array([[1, 2, 3], [3, 4, 5], [9, 6, 0]])

print("\nOriginal array:\n", a)
print("Transpose of array:\n", a.T)

# Python program to demonstrate
# unary operators in numpy
import numpy as np

arr = np.array([[1, 5, 6],
                [4, 7, 2],
                [3, 1, 9]])

# maximum element of array
print("Largest element is:", arr.max())
print("Row-wise maximum elements:",
      arr.max(axis=1))

# minimum element of array
print("Column-wise minimum elements:",
      arr.min(axis=0))

# sum of array elements
print("Sum of all array elements:",
      arr.sum())

# cumulative sum along each row
print("Cumulative sum along each row:\n",
      arr.cumsum(axis=1))

# Python program to demonstrate
# binary operators in Numpy
import numpy as np

a = np.array([[1, 2],
              [3, 4]])
b = np.array([[4, 3],
              [2, 1]])

# add arrays
print("Array sum:\n", a + b)

# multiply arrays (elementwise multiplication)
print("Array multiplication:\n", a * b)

# matrix multiplication
print("Matrix multiplication:\n", a.dot(b))

# Python program to demonstrate
# universal functions in numpy
import numpy as np

# create an array of sine values
a = np.array([0, np.pi / 2, np.pi])
print("Sine values of array elements:", np.sin(a))

# exponential values
a = np.array([0, 1, 2, 3])
print("Exponent of array elements:", np.exp(a))

# square root of array values
print("Square root of array elements:", np.sqrt(a))

# Python Program to create a data type object
import numpy as np

# np.int16 is converted into a data type object.
print(np.dtype(np.int16))

# Python Program to create a data type object
# containing a 32 bit big-endian integer
import numpy as np

# i4 represents integer of size 4 byte
# > represents big-endian byte ordering and
# < represents little-endian encoding.
# dt is a dtype object
dt = np.dtype('>i4')

print("Byte order is:", dt.byteorder)

print("Size is:", dt.itemsize)

print("Data type is:", dt.name)