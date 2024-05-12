# Write a python script to print first N odd natural numbers in reverse order. 

nNatural = int(input('Enter n number: '))

print(f'First {nNatural} Odd Numbers in Reverse Order:')
while(nNatural > 0):
    
    if(nNatural % 2 != 0):
        print(nNatural, end=" ")
    nNatural -=1