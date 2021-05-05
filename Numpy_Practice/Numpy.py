import numpy as np

# Create a vector with values ranging from 10 to 29
vector = np.arange(10,30)
print(vector)
# Output : [10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29]

# Create a vector with values ranging from 10 to 29 and reverse it
vector = np.arange(10,30)
vector = vector[::-1]
print(vector)
# Output : [29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10]

# create a 3*3 Matrix with 2 digit numbers
matrix = np.random.randint(10,100,9).reshape(3,3)
print(matrix)

# Find indices of non-zero elements from [1,9,0,0,4,0]
non_zero = np.nonzero([1,9,0,0,4,0])
print(non_zero)  # Output : array([0, 1, 4]

# Create 3*3 Identity Matrix
i = np.eye(3)
print(i)

# Create a 5*5 matrix with row value ranging 0 to 4
matrix = np.zeros(shape=(5,5))
matrix += np.arange(0,5)
print(matrix)
""" Output :
[[0. 1. 2. 3. 4.]
 [0. 1. 2. 3. 4.]
 [0. 1. 2. 3. 4.]
 [0. 1. 2. 3. 4.]
 [0. 1. 2. 3. 4.]]
"""
# np.add.reduce faster than np.sum
v = np.arange(1,11)
print(np.add.reduce(v))  # 55

# Check whether two arrays are equal
a = np.random.randint(10,100,10)
b = np.random.randint(10,100,10)
equal = np.allclose(a,b)
print(equal)

# Make an array immutable(read-only)
a = np.array([12,15,16,14,12,10,22])
a.setflags(write=False)
# a[3] = 999 # ValueError: assignment destination is read-only
print(a)

# subtract 2 from highest and add 2 into smallest value from an array
array = np.array([45,55,63,14,12,52,66,47,85,12,10])
array[array.argmax()] = array[array.argmax()] -2
array[array.argmin()] = array[array.argmin()] + 2
print(array)  # [45 55 63 14 12 52 66 47 83 12 12]
