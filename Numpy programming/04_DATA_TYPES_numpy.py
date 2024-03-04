import numpy as np

var = np.array([1,2,3,4])
print("Data type : ",var.dtype)

var = np.array([1.2,3.4,5.12, 3.12])
print("Data type : ",var.dtype)

var = np.array(["A", "B", "C", "D"])
print("Data type : ", var.dtype)

var = np.array(["A","B", "C","D", 1,2,3,4])
print("Data type : " ,var.dtype)

# converting one data type to another data type 

x = np.array([1,2,3,4], dtype="f")
print("Converted data type : ",x.dtype)
print(x)

x2 = np.array([1,2,3,4])
new = np.float32(x2)
print(x2)
print(new)

print("Data type : ",x2.dtype)
print("Data type : ",new.dtype)

new2 = np.int16(new)
print(new2)


new3 = np.string_(new2)
print(new3)


