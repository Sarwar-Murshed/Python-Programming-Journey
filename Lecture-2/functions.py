str1 = "I am learning python from Apna College"
print(str1.endswith("ega"))
print(str1.endswith("ege")) # returns True as it actually ends with 

str2 = "sarwar Murshed"

print(str2.capitalize())  # all characters will be small letter except the first one

# Replace Function ("Old","New") ---> replaces old string with the new one

print(str1.replace("python","Javascript"))

# find function()

print(str1.find("n"))         # --> as it exists in 9th index
print(str1.find("learning"))  # ---> string matches starting with 5th index
print(str1.find("xyz"))       # if str doesn't match then it will print -1

# count function 

print(str1.count("n"))   # counts how many times n exists in str1
print(str1.count("from"))