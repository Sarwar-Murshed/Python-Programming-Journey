# "Key" : "Value" ---> key can be string,int,float etc . Dict is mutable

student_info = {
    "Name" : "Sarwar Murshed",
    "Age"  : 23,
    "is_adult" : True,
    "Subject" : ["C","Python","Java"],
    "Topics"  : ("Dictionary","Set"),
    "Marks"   : 92.5
}

print(student_info)
print(type(student_info))    # returns dict type
print(student_info["Name"])
print(student_info["Subject"])
print(student_info["Marks"])

# changing the name

student_info["Name"] = "Sarwar"

# adding new key

student_info["Surname"] = "Sajan"

print(student_info)

# empty dictionary

null = {

}

print(null)

null["dict"] = "Null"
print(null)