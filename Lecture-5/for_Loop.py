"""
nums = [1,2,3,4,5]

for values in nums :
    print(values)

Fast_Food = ["Burger","Pizza","Taco","Sandwich","Hot dog","Shawarma"]   

for foods in Fast_Food :
    print(foods) 
 
""" 
# Q : 1,3,5,3,8,2,3,15,17,6 ---> search for a number x in this tuple using loop

nums = (1,3,5,3,8,2,3,15,17,6)
x = 3

idx = 0

for el in nums :
    if(el == x):
        print("Element found at index : ",idx)
    #   break --> for printing only first occurrence 
    idx +=1