# Write a python script to print first N natural numbers in reverse order. 

firstNum = 0 
nNatural = int(input(' Enter n numbers: '))

print(f'First {nNatural} Natural Numbers in Reverse Order:')
while(firstNum < nNatural):
    reverseNum = nNatural - firstNum
    print(reverseNum,end=" ")
    
    firstNum +=1
    