# # Array indexing is the same as accessing an array element 
# import numpy as np 

# a = np.array([5,6,7,3,4])
# print(a[2])

# # we can get the third and fourth elements from adding them 
# import numpy as np 

# a = np.array([5,6,7,3,4])
# print(a[1:5])
# print(f"Added value at position {a[2]} and {a[3]} is : " , a[2] + a[3])

# #  Accessing the 2-D - it is like a rows and columns 

# import numpy as np 

# a = np.array([[1,2,3,4,5],[6,7,8,9,10]])
# print("2nd element in the 1st row is : ", a[1][4])
# print(a[0][1] + a[1][3])

#  Accessing in 3-D 

import numpy as np

a = np.array([[[1,2,3], [4,5,6], [7,8,9]]])
print(a[0,2,2])