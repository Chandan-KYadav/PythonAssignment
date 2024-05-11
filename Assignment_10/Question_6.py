# Write a python script to print first N even natural numbers. (For loop)

nNumber = int(input('Enter Number : '))

iterable = range(1, (nNumber+1)*2)

print(f'First {nNumber} even natural numbers: ')
for e in iterable: 
    if e % 2 == 0 :
        print(e, end=" ")