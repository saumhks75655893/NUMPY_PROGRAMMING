# Now we will create numpy ndarray object 
# The array object in numpy is called ndarray 
# array()

import numpy as np 
from datetime import datetime

#  ------------------------------------  NUMPY   Vs   LIST  : ----------------------------------- #
''' 
Tradition list is slower than Numpy because it is developed using C language mostly and some in python language.
'''
# NumPy array : ----------
x = np.array([1,2,3,4,5])
print(x)
print(type(x))

# print value one by one
for i in x:
    print(i)

# list : ----------

y = [1,2,3,4,5]
print(y)
print(type(y))

m = np.arange(1,10)**2
print(m)


# DOT PRODUCT : -------------

a = [10, 20, 30]
b = [1,2,3]

'''  Tradition Python code to find dot product. '''
print()
def dot_product(a,b):
    result = 0
    for m,n in zip(a,b):
        result = result + m*n
    return result 

# before running the program time
before = datetime.now()

# running the program
for i in range(1000):
    dot_product(a,b)
    
# after running program time
after = datetime.now()

# printing time 
print('The time taken : ', after - before)

# Array importing : ---------

import array as arr

a = arr.array('i', [10,20,30])
print(type(a))

'''
Array module is not recommended to use because much library support is not available.

'''