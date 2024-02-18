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
# 1. array() 


# 2. arange()

import numpy as np
a = np.arange(30)
print(a)
b = np.arange(30).reshape(5,6)
print(b)
c = np.arange(27).reshape(3,9,3)
print(c)
