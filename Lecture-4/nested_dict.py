Student = {
   "Name"    : "Sarwar",
   "Subject" : {
     "OOP"   : 96,
     "DBMS"  : 94,
     "DSA"   : 98
   }
}

print(Student)

print(Student["Subject"])          # prints all subjects along with marks
print(Student["Subject"]["DBMS"])  # printing only DBMS marks