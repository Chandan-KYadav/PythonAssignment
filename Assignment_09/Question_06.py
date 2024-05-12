# Write a python script to print first N even natural numbers. 

num = 1 
nNatural = int(input('Enter n number: '))

print(f'First {nNatural} Even Numbers :')
while(num <= nNatural):
    
    if(num % 2 == 0):
        print(num, end=" ")
    num +=1