# Write a python script to print cubes of first N natural numbers. 

num = 1
nNatural = int(input(' Enter n number: '))

print(f'Cube of First {nNatural} Numbers')
while(num <= nNatural):
    cube = num * num * num
    print(f'Cube of {num} is {cube}')
    
    num += 1
