# write a recursive function to calculate the sum of first n natural numbers

n = int(input("Enter n : "))

def sum(n):
    if(n==0):
        return 0
    else:
        return n + sum(n-1)

total = sum(n)
print("Total : ",total)