import numpy as np
import random

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

a = np.array([1,2,3,4,5])
print(a)

a = np.array([[1,2,3], [4,5,6]])
print(a)

a = np.array([[[1,2,3]], [[4,5,6]],[[7,8,9]]])
print(a)

# 2. arange()

a = np.arange(30)
print(a)
b = np.arange(30).reshape(5,6)
print(b)
c = np.arange(15).reshape(1,5,3)
print(c)
print(c.shape)
print(c.size)

d = np.arange(10,35,3)
print(d)

# 3. zeros()

a = np.zeros((2,3))
print(a)

b = np.zeros((3,3))
print(b)

print(b.ndim)
print(b.shape)

# 4. ones()

s = np.ones((3,4))
print(s)

t = np.ones((3,3),dtype=np.complex64)
print(t)

# 5. linspace()

l = np.linspace(0,10,num=4)
print(l)

l = np.linspace(0,50,num=10)
print(l)

# 6. eye()

s = np.eye(3,3)
print(s)

# 7. random()

a = np.random.random((2,2))
print(a)

b = np.random.random((4,5))
print(b)
# 8. empty()

f = np.empty((2,3))
print(f)

# 9. full()

g = np.full((3,3),4)
print(g)