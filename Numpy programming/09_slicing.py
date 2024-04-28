import numpy as np 

SLICING : ----------

1-D array 
print()
print()

d1 = np.array([1,2,3,4,5,6,-1,-2,-3,-4,-5,-6])
print("From 0,1,2 : ",d1[0:3])
print("From start to end :",d1[:])
print("From start to end skipping one element :",d1[::2])
print("From start to less than 5 element :",d1[:5])
print("From 1 to 4 : ",d1[1:5:2])
print()
print("5 -2 : ", d1[4::3][0:2])

# 2-D array 

print()
print()
d2 = np.array([[1,2,3,4],[4,5,6,7]])
print("0's 0 to last : ",d2[0][0:])
print("0's, from  0 to end skipping one element : ",d2[0,::2])
print(d2[1,1:5])
print(d2[1,1:4:2])

# 3-d array 

print()
print()
d3 = np.array([[[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12]],
                
                [[-1,-2,-3,-4],
                 [-5,-6,-7,-8],
                 [-9,-10,-11,-12]]])

# print(d3)
# print(d3.shape)
# print()

print(d3[1,2,:])
print()
print(d3[0,2,:])
print()
print()

print(d3[1,:,:])
print()
print(d3[0,:,:])
print()
print()

print(d3[:,:,:])
print()
print()

print(d3[1:3,1,1])
print()
print(d3[0:3,1,1])
print()
print()

print("1 ka 1 to 2 ka 1 column (-6,-10):",d3[1,1:3,1])
print()
print("1 ka 1 to 2 ka 1 column (-6,-10):",d3[0,1:3,1])
print()
print()

print("1 ka 1 to 2 row tak , 1 to 2 column tak (-6 -7, -10 -11) : ",d3[1,1:3,1:3])
print()
print("1 ka 1 to 2 row tak , 1 to 2 column tak (-6 -7, -10 -11) : ",d3[0,1:3,1:3])
print()
print()

print(d3[1:3,1:3,1:3])
print()
print(d3[0:3,1:3,1:3])