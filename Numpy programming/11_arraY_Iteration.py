# Iteration

import numpy as np

# # one dimentional array : -

# a = np.array([1,2,3,4,5,6])
# print(a)

# for i in a:
#     print(i)


# # two - Dimentional array : --

# print()
# b = np.array([[1,2,3],[4,5,6]])
# for j in b:
#     print(j)

# print()

c = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[11, 12, 13], [14, 15, 16]],
    [[21, 22, 23], [24, 25, 26]]
]
)
# for j in c:
#     for i in j:
#         for k in i:
#             print(k, end=" ")


# # np.iter() function : ------------

# for i in np.nditer(c):
#     print(i)
    
# for i in np.nditer(c,flags=['buffered'],op_dtypes=["S"]):
#     print(i)

for i ,d in np.ndenumerate(c):
    print(i,' -> ',d)