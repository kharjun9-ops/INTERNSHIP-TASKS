print("Creating arrays")
import numpy as np
arr_1d = np.array([1, 2, 3, 4, 5])
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])

print("1D Array:\n", arr_1d)
print("2D Array:\n", arr_2d)

print("Shape of 2D Array:", arr_2d.shape)
print("Data Type:", arr_1d.dtype)

print("Mathematical operations")
import numpy as np
a = np.array([10, 20, 30, 40])
b = np.array([1, 2, 3, 4])

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Square of a:", a ** 2)

print("Array functions")
import numpy as np
numbers = np.array([12, 45, 78, 23, 56, 89])
print("Sum:", np.sum(numbers))
print("Mean (Average):", np.mean(numbers))
print("Maximum Value:", np.max(numbers))
print("Minimum Value:", np.min(numbers))
print("Standard Deviation:", np.std(numbers))