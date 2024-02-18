import numpy as np
import sys

a = np.array([10,20,30,40,50,10,20,30,40,50,10,20,30,40,50])
l = [10,20,30,40,50,10,20,30,40,50,10,20,30,40,50]

print("The Size of Numpy Array : ", sys.getsizeof(a))
print("The Size of List : ",sys.getsizeof(l))

'''
1. Numpy Arrays are superfase when compared with list. 
2. Numpy Arrays takes less space than the list. 
3. Numpy arrays are more convinient while performing mathematical operations.
'''

# Creation of Numpy Arrays : (Numpy library contains several funtions to create array based on our requirement .)

'''
Following are few of such functions : ----- 

1. array()
2. arange()
3. zeros()
4. ones()
5. linspace()
6. eye()
7. random()
etc. 

'''
