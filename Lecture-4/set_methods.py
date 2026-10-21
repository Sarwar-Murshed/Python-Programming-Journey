collection = set()
print("Empty",collection)

# 1. add() method

collection.add(1)
collection.add(2)
collection.add(3)
collection.add(2)
collection.add(4)
collection.add(7)
collection.add("Apna College")

print("After adding elements - ")
print(collection)

# 2 remove() method

collection.remove(4)
collection.remove(2)

print("After removing elements - ")
print(collection)

print("Length - ",len(collection))

# 3 clear() method --> clears the set (empty set)

collection.clear()

print("Empty",collection)
print("Length - ",len(collection))

# pop() method --> removes a random element

A = {"KFC","CFC","BFC",7,"Herfy","Fry Bucket",17}

print(A.pop())  # pops a random value
