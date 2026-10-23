# WAF to print the elements of a list is a single line (list is the parameter)

movies = ["Shutter Island","Titanic","Interstellar","Dune","Batman","Joker"]

def print_list(list):
    for item in list :
        print(item, end = " , ")

print_list(movies)