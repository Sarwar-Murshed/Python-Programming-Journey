# sum of first n numbers using while

n = int(input("Enter n : "))

i = 0
sum = 0

while(i<=n):
    sum +=i 
    i+=1

print("Sum = ",sum)  

# # using range
 
# n = int(input("Enter n : "))

# sum = 0 

# for i in range(1,n+1):
#     sum += i

# print("Sum = ",sum)    