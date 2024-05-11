# Write a python script to print cube of first N natural numbers. (For loop)

nNumber = int(input('Enter Number : '))

iterable = range(1, nNumber+1)

print(f'Cube of First {nNumber} Natural Numbers: ')
for e in iterable: 
    cube = e * e * e
    print(f'Cube of {e} is {cube}')