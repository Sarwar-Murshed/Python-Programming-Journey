# multi dimensional

import numpy as np

# 0 dimensional array

arr = np.array('A')
print("No. of dimension : ",arr.ndim)

# 1 dimensional array

arr2 = np.array(['A','B','C'])           # list
print("No. of dimension : ",arr2.ndim)

# 2 dimensional array

arr3 = np.array([['A','B','C'],
                 ['D','E','F'],
                 ['G','H','I']])   

print("No. of dimension : ",arr3.ndim)

# 3 dimensional array

arr4 = np.array([[['A','B','C'],['D','E','F'],['G','H','I']],
                 [['J','K','L'],['M','N','O'],['P','Q','R']],
                 [['S','T','U'],['V','W','X'],['Y','Z',' ']]])   

print("No. of dimension : ",arr4.ndim)
print("Array 4 shape : ",arr4.shape)

arr5 = np.array([[['A','B','C'],['D','E','F'],['G','H','I']],
                 [['S','T','U'],['V','W','X'],['Y','Z',' ']]]) 
print("Array 5 shape : ",arr5.shape)

print(arr4[1][2][1])   # arr[row][column][index]\
print(arr4[2][1][1])

# another way

print(arr5[1,1,1])
print(arr4[1,2,0])

# printing my name

x = arr4[2,0,0] + arr4[0,0,0] + arr4[1,0,0] + arr4[0,0,0] + arr4[1,1,1]
print(x)