import numpy as np 

''' 
By using shape : --
1. we can know the no. of rows and columns used in the array. 

'''

b = np.eye(4)
print(b)
print(b.shape)

d = np.array([1,2,3,4],ndmin=4)
print(d)
print(d.shape)

print(d.ndim)


print()


''' 
By using reshape 
1. we can reshape the array means we can change the dimensions (also rows and columns)'''

c = np.array([10,11,12,20,30,40,50,60,70,80,90,100])
x = c.reshape(4,3)
print(x)

a = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
b = a.reshape(4,4)
print(a)
print()
print(b)

