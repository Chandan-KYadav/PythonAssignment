# Write a python script to create list of first N even numbers. 

list_of_even_num = []

N_even = int(input('Enter N numbers: '))

i = 1

while(i <= (N_even *2)):
    
    if i % 2 == 0:
        list_of_even_num.append(i)
    
    i += 1
    
print(list_of_even_num)