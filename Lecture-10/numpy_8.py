# matrix 

import numpy as np 

arr1 = np.array([[1,2,3,4]])          # 1 row, 4 columns (1,4)
arr2 = np.array([[1],[2],[3],[4]])    # 4 row, 1 columns (4,1)

print(arr1.shape)
print(arr2.shape)

# multiplying ,size will be (4,4)

arr3 = arr1 * arr2

print(arr3)
print(arr3.shape)