# Write a python script to print first 10 multiples of N. 

num = 1
nNumber = int(input(' Enter n number: '))
while(num <= 10):
    multiple = nNumber * num 
    print(f'{nNumber} X {num} = {multiple}')
    
    num += 1
