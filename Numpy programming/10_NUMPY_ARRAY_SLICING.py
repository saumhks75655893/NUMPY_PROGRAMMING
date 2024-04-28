# NumPy Array slicing : ------------
# Slicing : slicing in python means taking elements from one given index to another index. 
# [start : end], [start : end : step]

# now we will slice an element from the array. 

import numpy as np 

a = np.array([1,2,3,4,5,6,7,8,9,10])
print("From 1 to 4 : ",a[1:5])

#  without last index value 

print("from 4 to 1 : ",a[4:])

print("From start to less than 8 : ",a[:8])

print("From -8 to less than 1 : ",a[-8:])

#  with step value : -------

print("From start to end skipping one element : ",a[::2])

print("From 1 to 4 skipping one element : ",a[1:5:2])

#  slicing on 2-D array : -----------
print()

import numpy as np 

a = np.array([[1,2,3,4,5],[6,7,8,9,10]])

print("Second row : From 1 to less than 4 : (2d array ) : ",a[1,1:4])

#  from both list : slicing from both list their elements : --------
print()
print(a[0:2, 2])
print()
print(a[0:2, 0:2])
print()
print(a[0:2, 3:])