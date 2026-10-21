# immutable that can not be changed tuple( , )

tup = (1)
print(type(tup))         # int type as there's no comma

tup2 = (1,)
print(type(tup2))        # tuple type 

tupl = (12,17,5,3,19)
print(tupl)
print(tupl[0])

# tupl[0] = 31  --> error cz it is immutable , can not be changed

# slicing

print(tupl[1:3])