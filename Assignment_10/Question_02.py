# Write a python script to print first 10 multiple of N. (For loop)

nNumber = int(input('Enter n Number : '))
iterable = range(1, 11) # range(beg, end, difference)

print(f'First 10 Multiple of {nNumber}')
for e in iterable:
    multiple = nNumber * e 
    print(f'{nNumber} X {e} = {multiple}')
