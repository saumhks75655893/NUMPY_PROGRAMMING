'''
ARITHMETIC OPERATIONS : ----------

np.add(a,b)
np.substract(a,b)
np.multiply(a,b)
np.divide(a,b)
np.mod(a,b)
np.power(a,b)
np.reciprocal(a)

'''
import numpy as np 

# 1. ADDITION : ----------
a = np.array([1,2,3,4,5])
varadd = a + 3
print(varadd)

b = np.array([6,7,8,9,10])
varadd = a + b
print(varadd)

print()
print()
# 2. SUBSTRACTION : --------
a = np.array([1,2,3,4,5])
varsub = a - 3
print(varsub)

b = np.array([6,7,8,9,10])
varsub = a - b
print(varsub)

print()
print()
# 3. MULTIPLICATION : -----------
a = np.array([1,2,3,4,5])
varmul = a * 3
print(varmul)

b = np.array([6,7,8,9,10])
varmul = a * b
print(varmul)

print()
print()
# 4. DIVISION : ------------
a = np.array([1,2,3,4,5])
vardiv = a / 3
print(vardiv)

b = np.array([6,7,8,9,10])
vardiv = b // a
print(vardiv)

print()
print()
# 5. MODULUS : ------------

a = np.array([1,2,3,4,5])
varmod = a % 2
print(varmod)

print()
print()

# 6. RECIPROCAL 

a = np.array([1,2,3,4])
varrec = np.reciprocal(a)
print(varrec)

print()
print()

#  ARITHMETIC FUNCTION : -------------

'''
1. np.min()
2. np.max()
3. np.argmin()
4. np.sqrt()
5. np.sin()
6. np.cos()
7. np.cumsum()

'''

a = np.array([1,2,3,4,5])
min = np.min(a)
print("Min : " , min)

argmin = np.argmin(a)
print("Min value positon  : ", argmin)

max = np.max(b)
print("Max : " , max)

argmax = np.argmax(a)
print("Max position : ",argmax)

sqrt = np.sqrt(a)
print("Square : ",sqrt)

cos1 = np.cos(a)
print("Cos : ",cos1)

sin1 = np.sin(a)
print("Sin : ", sin1)

cumsum1 = np.cumsum(a)
print("Cumsum : ",cumsum1)


#  axis = 0 --> for the evaluating value according to the column
#  axis = 1 --> for the evaluating value according to the row

# row
a = np.array([[1,2,3,4],[5,6,7,8]])
min2d = np.min(a, axis=1)
print("Min 2d row wise : ", min2d)

# column
a = np.array([[1,2,3,4],[5,6,7,8]])
min2d = np.min(a, axis=0)
print("Min 2d column wise : ", min2d)