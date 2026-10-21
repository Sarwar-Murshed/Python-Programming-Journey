student_info = {
    "Name" : "Sarwar Murshed",
    "Age"  : 23,
    "is_adult" : True,
    "Subject" : ["C","Python","Java"],
    "Topics"  : ("Dictionary","Set"),
    "Marks"   : 92.5
}

# 1. printing all keys  --> keys() method

print(student_info.keys())

# printing all keys in list format  --> surrounded by [] bracket

print(list(student_info.keys()))

# printing all keys in tuple format  --> surrounded by () bracket

print(tuple(student_info.keys()))

# printing total number of keys

print("Total keys : ",len(student_info.keys()))

# 2. printing all values --> values() method

print(student_info.values())
print(list(student_info.values()))

# 3 items() method

print(student_info.items())
pair = list(student_info.items())
print(pair[1])

# 4 get() method --> returns the key according to the value

print(student_info["Name"])
print(student_info.get("Name"))

# print(student_info["Name2"])  --> gives error
# print(student_info.get("Name2")) --> no error, gives none

# 5 update() method

student_info.update({"City" : "Dhaka"})
print(student_info)



"""
1. keys() method   ---> prints all keys
2. values() method ---> prints all values
3. items() method  ---> prints key & value separately 
4. get() method    ---> returns the key according to the value
5. update() method ---> inserts the specified items to the dictionary

"""