f = open("Lecture-7-File/demo.txt", "r")
data = f.read()
print(data)
print(type(data))
f.close()



# line1 = f.readline()  --> will print the line 1
#  print(line1)    
# f.read(5)  --> first 5 characters will read

# with open("demo.txt", "r") as f:
#     data = f.read()
#     print(data)

# with open("demo.txt", "w") as f:
#     f.write("new data")