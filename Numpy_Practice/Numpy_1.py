import numpy as np

# How to find the closet value to a given scalar in an array
a = np.arange(100)
b = np.random.uniform(0,100)
index = (np.abs(a-b)).argmin()
print(index)

# Change the datatype of numpy array
array = np.arange(1,11,dtype=np.int32)
array = array.astype(np.float32, copy=False)
print(array)

# What is the equivalent of enumerate for numpy arrays?
array = np.random.randint(1,100,25).reshape(5,5)
for index, values in np.ndenumerate(array):
    print(index, values)

# How to sort an array by nth column
array = np.random.randint(1,100,25).reshape(5,5)
print(array)
print(array[array[:,1].argsort()])  # Sorted by Second column
print(array[array[:,2].argsort()]) # Sorted by third column

# How to swap Two rows of an array
print("***************************************")
array = np.random.randint(1,100,25).reshape(5,5)
print(array)
array[[0,1]] = array[[1,0]] # Swap First and Second Row
print(array)
array[[2,4]] = array[[4,2]] # Swap Third and Fifth Row
print(array)

# How to Find most frequent value of an array
print('***************************************')
array = np.random.randint(1,20,25)
print(array)
print(np.bincount(array).argmax())

# How to get the Block Sum of 16*16 Array (Block Size : 4*4)
print('***************************************')
array = np.random.randint(1,100,256).reshape(16,16)
block_size = 4
summation = np.add.reduceat(
                            np.add.reduceat(array,np.arange(0,array.shape[0], block_size),axis=0),
                                            np.arange(0,array.shape[1], block_size),axis=1)
print(array)
print(summation)

