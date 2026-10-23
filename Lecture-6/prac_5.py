# WAF to print if n is even it'll return "Even" string. else, it'll return "Odd" string

n = int(input("Enter n : "))

def Checking_Even_Odd_fun(n):
    if(n % 2 == 0):
        print("Even")
    else:
        print("Odd")

Checking_Even_Odd_fun(n)
