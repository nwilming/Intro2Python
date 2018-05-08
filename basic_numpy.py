'''
Introduction to python: Numpy / Scipy / Matplotlib
'''

import numpy as np

'''
No. 1: Creating numpy arrays
'''

v = np.array([1,2,3,4])  # a vector
v

M = np.array([[1,2],[3,4]]) # a matrix
M

type(v), type(M) # object type

v.shape, M.shape # the shape is different

v.size, M.size # same number of elements

M.dtype # data type

M[0,0] = "hello" # does not work

M = array([[1, 2], [3, 4]], dtype=complex) # define the type of the array data (common type are: int, float, complex, bool, object)
M


'''
No. 2: Array generating functions
'''

x = np.arange(0, 10, 1) # creates a range. arguments: start, stop, step
x

x = np.linspace(0, 10, 25) # creates a range. arguments: start, stop, num
x

x = np.logspace(0, 10, 10, base=np.e) # creates a range in log-space. arguments: start, stop, num
x

x = np.random.rand(5,5) # uniform random numbers in [0,1]. arguments: shape
x

x = np.random.randn(5,5) # standard normal distributed random numbers. arguments: shape
x

x = np.diag([1,2,3]) # a diagonal matrix. arguments: array (if 2D, the diag is returned)
x

x = diag([1,2,3], k=1) # diagonal with offset from the main diagonal. arguments: array, offset
x

x = np.zeros((3,3)) # zeros
x

x = np.ones((3,3)) # ones
x

x = np.ones((3,3), dtype=bool) # boolean data type
x


'''
No. 3: Manipulating arrays
'''

# INDEXING:

v[0] # v is a vector, and has only one dimension, taking one index

M[1,1] # M is a matrix, or a 2 dimensional array, taking two indices 

M[1,:] # row 1

M[:,1] # column 1

M[0,0] = 1 # assign new values to elements in an array using indexing
M

M[1,:] = 0 # also works for rows
M[:,2] = -1 # and columns

# INDEX SLICING:

v = np.arange(8)
v

v[1:3] # lower:upper:step

v[1:3] = [-2,-3] # assign new values to elements in an array using slicing
v

v[::] # lower, upper, step all take the default values

v[::2] # step is 2, lower and upper defaults to the beginning and end of the array

v[:3] # first three elements

v[3:] # elements from index 3

v[-1] # the last element in the array

v[-3:] # the last three elements

M = np.arange(16).reshape((4,4))
M

M[1:3, 1:3] # a block from the original array

M[::2, ::2] # strides

# FANCY INDEXING

row_indices = [1, 2, 3] # fancy indexing is the name for when an array or list is used in-place of an index:
M[row_indices]

col_indices = [1, 2, -1] # remember, index -1 means the last element
M[row_indices, col_indices]

mask = np.array([1,0,1,0,0,1,1,0], dtype=bool) # We can also use index masks: If the index mask is an Numpy array of data type bool, then an element is selected (True) or not (False) depending on the value of the index mask at the position of each element
mask
v[mask]

mask = (M>2) & (M < 13) # conditionally select elements from an array, using for example comparison operators
mask
M[mask]

indices = np.where(mask) # the index mask can be converted to position index using the where function
indices
M[indices]


'''
No. 4: Linear algebra
'''

# ELEMENT-WISE ARRAY-ARRAY OPERATIONS

v = np.arange(4)
M = np.arange(16).reshape((4,4))

M * 2 # use the usual arithmetic operators to multiply, add, subtract, and divide arrays with scalar numbers
M + 2

M * M # when adding, subtracting, multiplying and dividing arrays with each other, the default behaviour is element-wise operations
M + M

M * v # when adding, subtracting, multiplying and dividing arrays with compatible shapes, we get an element-wise multiplication of each row
M + v

# MATRIX ALGEBRA

np.dot(M, M) # matrix-matrix multiplication

np.dot(M, v) # matrix-vector multiplication

np.dot(v, v) # inner vector multiplication

M = matrix(M) # cast to matrix
M

v = matrix(v).T # cast to matrix; make it a column vector via transpose
v

M * M # matrix-matrix multiplication

M * v # matrix-vector multiplication

v.T * v # inner vector multiplication

v * M # if we try to add, subtract or multiply objects with incomplatible shapes we get an error

# MATRIX COMPUTATIONS

np.linalg.inv(M) # inverse

np.linalg.det(M) # determinant


'''
No. 4: Data processing
'''

M = np.arange(16).reshape((4,4))

np.mean(M)

M.mean()

np.mean(M, axis=0)

M.mean(axis=0)

M.mean(axis=1)

np.median(M)

np.std(M)

np.var(M)

np.min(M)

np.max(M)

np.sum(M) # sum up all elements

np.cumsum(M) # cummulative sum

np.prod(M + 1) # product of all elements

np.cumprod(M+1) # cummulative product


'''
No. 5: Reshaping, resizing and stacking arrays
'''

v = array([[1, 2, 3, 4]])
v2 = array([[11, 12, 13, 14]])
M = np.arange(16).reshape((4,4))

n, m = M.shape # make into vector:
M.reshape((1,n*m))

M.flatten() # make into vector

M.reshape((2,8)) # reshape into 2 rows, 8 columns

np.repeat(v, 3) # repeat each element 3 times

np.tile(v, 3) # tile the matrix 3 times 

np.concatenate((v, v2)) # concatenate 2 vectors (default across first dimension)

np.concatenate((v, v2), axis=1) # concatenate 2 vectors across second dimension

np.vstack((M,v)) # stack vertically

np.hstack((M,v)) # stack horizontally --> dimension mismatch

np.hstack((M,v.T)) # stack horizontally 

