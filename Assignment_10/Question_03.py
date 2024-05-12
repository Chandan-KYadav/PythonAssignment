# Write a python script to print first M multiples of N. (For loop)

mTimes = int(input('Enter M times: '))
nNumber = int(input('Enter N Number: '))
iterable = range(1, mTimes+1)

for e in iterable:
    
    multiple = nNumber * e 
    print(f'{nNumber} X {e} = {multiple}')
    