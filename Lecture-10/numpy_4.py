import numpy as np 

arr = np.array([[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12],
                [13,14,15,16]])

# slicing([start][end][step]) 

#print(arr[1:3])   # printing indexing 1 to 2

#print(arr[2:4])   # printing indexing 2 to 3

print(arr[::-1])   # printing reverse index
print()
print(arr[::-2])   # printing reverse index +2
print()

print(arr[:,0])   # printing column 0
print()
print(arr[:,3])   # printing column 3
print()
print(arr[:, 1:3])  # printing column 1 to 2

# printing sub matrix

print()
print(arr[2: , 2:])  # starts with row 2, row 2's, index 2 to rest of the elements

print()
print(arr[1:3 , 2:]) # row 1 to 2, starts with index 2

