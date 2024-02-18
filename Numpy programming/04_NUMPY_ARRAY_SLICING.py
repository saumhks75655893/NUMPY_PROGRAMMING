# NumPy Array slicing : ------------
# Slicing : slicing in python means taking elements from one given index to another index. 
# [start : end], [start : end : step]

# now we will slice an element from the array. 

import numpy as np 

a = np.array([1,2,3,4,5,6,7,8,9,10])
print(a[1:5])

#  without last index value 

print(a[4:])

print(a[:8])

print(a[-8:])

#  with step value : -------

print(a[::2])

print(a[1:5:2])

#  slicing on 2-D array : -----------

import numpy as np 

a = np.array([[1,2,3,4,5],[6,7,8,9,10]])

print(a[1,1:4])

#  from both list : slicing from both list their elements : --------

print(a[0:2, 2])
print(a[0:2, 0:2])
print(a[0:2, 3:])