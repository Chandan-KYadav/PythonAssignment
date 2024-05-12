# Write a python script to print first N odd natural number. (For loop)

nNumber = int(input('Enter Number : '))

iterable = range(1, (nNumber)*2)

print(f'First {nNumber} odd natural numbers: ')
for e in iterable: 
    if e % 2 != 0 :
        print(e, end=" ")