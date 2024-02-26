import numpy as np

# arithmetic operations 

var = np.array([1,2,3,4])
varadd = var + 3
print(varadd)

var2 = np.array([10,20,30,40])
varadd = var + var2
print(varadd)

var3 = np.array([[1,2,3,4],[5,6,7,8]])
var4 = np.array([[9,10,11,12],[13,14,15,16]])

var2dadd = var3 + var4
print(var2dadd)

var3 = np.array([[1,2,3,4],[5,6,7,8]])
var4 = np.array([[9,10,11,12],[13,14,15,16]])

var2dsub = var3 - var4
print(var2dsub)

var3 = np.array([[1,2,3,4],[5,6,7,8]])
var4 = np.array([[9,10,11,12],[13,14,15,16]])

var2dmul = var3 * var4
print(var2dmul)

var3 = np.array([[1,2,3,4],[5,6,7,8]])
var4 = np.array([[9,10,11,12],[13,14,15,16]])

var2ddiv = var3 / var4
print(var2ddiv)

# arithmetic functions : ---------

var = np.array([1,2,3,4,5,0,10])

print("Min value : ",np.min(var))
print("Max value : ",np.max(var))
print("Argmin value : ",np.argmin(var))
print("Argmax value : ",np.argmax(var))
print("Sqrt value : ",np.sqrt(var))
print("Sin value : ",np.sin(var))
print("Cos value : ",np.cos(var))
print("Cumsum value : ",np.cumsum(var))

# for 2-d array : ---------

var = np.array([[1,2,3,4,5],[6,7,8,9,10]])

print("Min value : ",np.min(var, axis=0))
print("Min value : ",np.min(var, axis=1))
print("Max value : ",np.max(var, axis=0))
print("Max value : ",np.max(var, axis=1))
print("Sin value : ",np.sin(var))
print("Cos value : ",np.cos(var))