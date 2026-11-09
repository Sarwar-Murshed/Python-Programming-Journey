# aggregate functions

import numpy as np 

arr = np.array([[1,2,3,4,5],
                [6,7,8,9,10]])

# print("Sum :",np.sum(arr))
# print("Mean :",np.mean(arr))
# print("Max :",np.max(arr))
# print("Min :",np.min(arr))
# print("Standard Deviation :",np.std(arr))
# print("Variance :",np.var(arr))
# print("Max value idx :",np.argmax(arr))
# print("Min value idx :",np.argmin(arr))

#printing all columns

print(np.sum(arr , axis = 0))

#printing all rows

print(np.sum(arr , axis = 1))
