# Write a python script to print table of user's choice. (For Loop)

nNumber = int(input('Enter Table Number: '))
iterable = range(1, 11)

for e in iterable:
    
    multiple = nNumber * e 
    print(f'{nNumber} X {e} = {multiple}')
