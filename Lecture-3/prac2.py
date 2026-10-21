# WAP to check if a list contains a palindrome of elements ( hint : use copy( method() )

list_1 = [1,3,5,3,1]
list_2 = [1,7,8,2,0]
list_3 = ["m","a","d","a","m"]

copy_list_1 = list_1.copy()

copy_list_1.reverse()

if( list_1 == copy_list_1):
    print("List 1 is Palindrome")
else :
    print("List 1 is not Palindrome") 

copy_list_2 = list_2.copy()    

copy_list_2.reverse()

if(list_2 == copy_list_2) :
    print("List 2 is Palindrome")
else :
    print("List 2 is not Palindrome")    
 
copy_list_3 = list_3.copy()

copy_list_3.reverse()

if(list_3 == copy_list_3):
    print("List 3 is Palindrome")
else :
    print("List 3 is not Palindrome")    