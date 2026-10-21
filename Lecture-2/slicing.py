str1 = "Sarwar Murshed"

print("Prints 1 to 3 charcters : ",str1[1 : 4])
print("Prints 3 to last charcters : ",str1[3 : ])
print("Prints start to 5th charcters : ",str1[ : 6])
print("Prints 5 to last charcters : ",str1[5 : len(str1)])

print("\nNegative Index")
str2 = "Banana"

print(str2[-4 : -1 ]) # backward index starts with -6

# print-->str[1 : 4] determines that it will print the character between index 1 to 4-1 =3
