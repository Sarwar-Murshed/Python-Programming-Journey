# def calc_sum(x,y):
#     sum = x + y
#     print(sum)
#     return sum

# calc_sum(5,10)
# calc_sum(2,7)
# calc_sum(17,32)

# avg of 3 numbers

def calc_avg(a,b,c):
    avg = (a+b+c)/3
    return avg

num1 = float(input("Enter number 1 : "))
num2 = float(input("Enter number 2 : "))
num3 = float(input("Enter number 3 : "))

result = calc_avg(num1,num2,num3)


print(result)