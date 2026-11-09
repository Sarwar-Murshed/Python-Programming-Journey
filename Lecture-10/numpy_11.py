# random numbers

import numpy as np

arr = np.random.default_rng()

print(arr.integers(1,6))  # gives any random values from 1 to 5
print(arr.integers(low = 1 , high = 10))  
print(arr.integers(low = 1 , high = 100, size = (3,2)))  # 3 rows, 2 columns

print()
# floating value (uniform)

print(np.random.uniform(low = -1, high = 1, size = (2,2)))
print()

# shuffle array

ran = np.random.default_rng()
arr2 = np.array([1,3,5,7,9])
ran.shuffle(arr2)
print(arr2)