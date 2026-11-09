import numpy as np

f = np.random.default_rng()

fruits = np.array(["apple", "orange", "banana", "coconut", "pineapple"])

# fruits = f.choice(fruits, size=3)  picks 3 random fruits

fruits = f.choice(fruits, size=(3, 3))

print(fruits)