# Write a python script to print first N odd natural numbers. 

num = 1
i = 0
nNatural = int(input(' Enter n numbers: '))

print(f'First {nNatural} Odd Natural Numbers:')
while(i < 10):
    print(num , end=" ")
    num = num + 2

    i +=1