# Write a python script to print square of first N natural numbers. (For loop)

nNumber = int(input('Enter Number : '))

iterable = range(1, nNumber+1)

print(f'Square of First {nNumber} Natural Numbers: ')
for e in iterable: 
    square = e * e
    print(f'Sqare of {e} is {square}')