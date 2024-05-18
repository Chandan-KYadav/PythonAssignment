# Write a python program to multiply all the numbers in a list. 

def multiplication (args):
    result = 1
    
    for e in args:
        result *= e
        
    return result

list1 = [10, 15, 90, 45, 68]

multiply_all = multiplication(list1)

print(multiply_all)