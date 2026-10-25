f = open("Lecture-7-File/sample2.txt","r+")
f.write("hello")
print(f.read())
f.close()

f = open("sample2.txt", "a+")

f.write(" Hello")

f.seek(0)
print(f.read())

f.close()