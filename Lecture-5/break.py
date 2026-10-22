# i = 1

# while(i<=5):
#     print(i)
#     if(i==3):
#         break
#     i+=1    
# print("Loop ended")    

# 1,4,9,16,25,36,49,64,81,100 --> tuples (search)

nums = (1,4,9,16,25,36,49,64,81,100)

x = int(input("Enter x : "))

i = 0

while(i < len(nums)):
    if(x == nums[i]):
        print("Found at index ",i)
        break
    else :
        print("Not found")    
    i+=1