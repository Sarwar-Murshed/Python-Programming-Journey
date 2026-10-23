# write a recursive function to print all elements in a list (use list and idx as a parameter)

def print_list(list,idx):
    if(idx == len(list)):
        return
    
    print(list[idx])
    print_list(list,idx+1)

fruits = ["Mango","Apple","Banana","Jackfruit","Orange"]

print_list(fruits,0)