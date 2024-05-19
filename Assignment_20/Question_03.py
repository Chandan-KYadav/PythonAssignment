# Write a python program to create a function that prints the even numbers from a given list. sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def even_number (parm):
    for e in parm:
        if e % 2 == 0:
            print(e,end=" ")
        
# Drive Code
sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even_number(sample_list)