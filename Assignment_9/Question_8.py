# Write a python script to print squares of first N natural numbers. 

num = 1
nNatural = int(input(' Enter n number: '))

print(f'Square of First {nNatural} Numbers')
while(num <= nNatural):
    square = num * num 
    print(f'Square of {num} is {square}')
    
    num += 1
    
    