# ------------          - :  NumPy Array Data Type : -       -----------

import numpy as np 
a = np.array([1,2,3,4,5,6,7,8,9,10])
print(a)

print(a.dtype)

b = np.array(['apple','banana','cherry'])
print(b.dtype)

#  creating an array with a defined data type : ----

a = np.array([1,2,3,4],dtype='S')
print(a)
print(a.dtype)

#  Now we will create an array with data type 4 byte integer : -----

b = np.array([1,2,3,4],dtype='i4')
print(b)
print(b.dtype)

# converting an string to int which cann't be changed : ----

d = np.array(['a','1','2'], dtype='i')
print(d.dtype)

# Converting data type in existing array  -   using : astype() : -------

import numpy as np
d = np.array([1.1,2.2,3.3])
d1 = d.astype('i')
print(d1)
print(d1.dtype)

# Converting data type in existing array  -   using : astype() : -------

import numpy as np
d = np.array([1,0,3])
d1 = d.astype(bool)
print(d1)
print(d1.dtype)


