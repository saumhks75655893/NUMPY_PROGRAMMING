# Now we will create numpy ndarray object 
# The array object in numpy is called ndarray 
# array()

import numpy as np 
import timeit

#  ------------------------------------  NUMPY   Vs   LIST  : ----------------------------------- #
''' Tradition list is slower than Numpy because it is developed using C language mostly and some in python language.
'''
# NumPy array : ----------
x = np.array([1,2,3,4,5])
print(x)
print(type(x))

# list : ----------

y = [1,2,3,4,5]
print(y)
print(type(y))

m = np.arange(1,10)**2
print(m)

