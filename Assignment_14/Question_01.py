# Write a python script to create a list of first N natural numbers. 

list_of_natural_num = []

N_number = int(input('Enter N number : '))

i = 1 

while(i <= N_number):
    list_of_natural_num.append(i)
    
    i += 1 

print(list_of_natural_num)