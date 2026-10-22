# skipping odd values using continue key word

i=1
while(i<=10):
    if(i % 2 != 0):
        i+=1
        continue
    print(i)
    i+=1    