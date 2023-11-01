# We can also pass a list, tuple or any array like object with array(). and it will be converted to ndarray. 

import numpy as np

y = np.array((1,2,3,4,5))
print(y)
print(type(y))

#---------------------------------- :  DIMENSIONS IN ARRAYS  : -----------------------------------------------#
'''
A dimensions in Array is one level of array depth ( nested array )
'''

# 0 - D => Scalars , are the elements in an array ,  each value in an array is a 0-D array. 

# Now we will create 0-D array with value 42
import numpy as np 

x = np.array(42)
print(x)

#  1 - D => An array that has 0-D as its elements is called unidirectional or 1-D

import numpy as np 

y = np.array([1,2,3,4,5])
print(y)

#  Creat  2-D array containing 2 Arrays with certain values. 

import numpy as np 

x = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(x)

#  Now we will create a 3-D array with two 2-D array. 

import numpy as np

himanshu = np.array([[[1,2,3], [4,5,6],[7,8,9]]])
print(himanshu)



#  Check how many dimensions the array have : ndim attribute . 

import numpy as np 

a = np.array(42)
b = np.array([1,2,3,4])
c = np.array([[1,2,3,4,5], [6,7,8,9,10]])
d = np.array([[[1,2,3], [4,5,6],[7,8,9]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

# Create an array with 5 dimensions and varify that it has 5 dimensions 

import numpy as np

him = np.array([1,2,3,4,5],ndmin=5)
print(him)
print('Number of dimension : ',him.ndim)

a = np.array([0,1,2,3,4,5])
b = a.reshape(3,2)
print(b)
