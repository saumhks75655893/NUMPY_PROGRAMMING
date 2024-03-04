import numpy as np 

var1 = np.array([1,2,3,4,5])
print(var1)
print(var1.shape)
print()
print()


var2 = np.array([[1],[2],[3],[4],[5]])
print(var2)
print(var2.shape)
print()
print()
varadd = var1 + var2

print(varadd)

# new 

var1 = np.array([[1],[2]])
print(var1.shape)

var2 = np.array([[1,2,3],[4,5,6]])
print(var2.shape)

varadd = var1 + var2
print(varadd)