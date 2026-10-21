# set is the collection of the unordered items. Each element in the set must be unique and 
# immutable. list and dict can not be used as it is mutable

collection1 = {1,2,3,4}
print(collection1)
print(type(collection1))   # set

collection2 = {1,2,3,2,5,"Hello","World","Hello"}
print(collection2)      # removes duplicate values
print(len(collection2)) # does not count one same value twice times

# empty set syntax --> x = set()

x = set()  # if we use {} this bracket, then it will be an empty dict
print(type(x))

# sets are mutable but elements of set is immutable