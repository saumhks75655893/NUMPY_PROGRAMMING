#  Difference between numpy array copy and view : ----------
# We will make a copy, change in original array and display both. 

import numpy as np
d = np.array([1,2,3,4])
d1 = d.copy()
d[0] = 41
print(d)
print(d1)

# now we will make a view, change in origin array and display both array 

import numpy as np
d = np.array([1,2,3,4])
d1 = d.view()
d[0] = 42
print(d)
print(d1)
