# filtering

import numpy as np

ages = np.array([[21,18,27,7,72,16,33],[65,53,81,78,39,47,9]])

teenagers = ages[ages < 18]
adults = ages[(ages >= 18) & (ages < 65)]
seniors = ages[ages >= 65]

print("Teenagers :",teenagers)
print("adults : ",adults)
print("Seniors :",seniors)

evens = ages[(ages % 2 == 0)]
odds = ages[(ages % 2 != 0)]

print("Even ages :",evens)
print("Odd ages : ",odds)
