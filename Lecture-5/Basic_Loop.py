"""
#1 printing hello 5x times with count

count = 1
while count <= 5 :
    print("Hello")
    count+=1

print(count)

#2 printing 20 to 1

i = 20

while (i>=1) :
    print(i)
    i-=1

#3 multiplication of n

n = int(input("Enter n : "))

i = 1
while(i<=10):
  print(n,"*",i,"=",n*i)
  i+=1


#4 square of 1 to 10

i = 1

while(i<=10):
    print(i*i)
    i+=1

"""

# 1,4,9,16,25,36,49,64,81,100 --> tuples (search)

nums = (1,4,9,16,25,36,49,64,81,100)

x = int(input("Enter x : "))

i = 0

while(i < len(nums)):
    if(x == nums[i]):
        print("Found at index ",i)
    else :
        print("Not found")    
    i+=1