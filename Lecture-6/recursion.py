"""
# printing n to 0

n = int(input("Enter n : "))

def show(n):
    if(n < 0):
        return
    print(n)      # if i flip line 7 & 8, then it will print 0 to n
    show(n-1)

show(n)    

"""

# factorial using recursion

n = int(input("Enter n : "))

def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)

fact = factorial(n)

print("Factorial of",n,"=",fact)

