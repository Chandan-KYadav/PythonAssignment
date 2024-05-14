# Write a python script to create list of first N odd numbers. 

list_of_odd_num = []

N_odd = int(input('Enter N numbers: '))

i = 1

while(i <= (N_odd *2)):
    
    if i % 2 != 0:
        list_of_odd_num.append(i)
    
    i += 1
    
print(list_of_odd_num)