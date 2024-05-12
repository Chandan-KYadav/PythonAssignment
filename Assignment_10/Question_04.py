# Write a python script to print first 10 multiples of N in reverse order. (For Loop)

nNumber = int(input('Enter Number: '))

iterable = range(10, 0 , -1)

print(f' first 10 multiple of {nNumber} numbers in reverse order: ')
for e in iterable:
    
    multiple = nNumber * e 
    print(f'{nNumber} X {e} = {multiple}')