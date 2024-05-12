# Write a python script to print first N natural numbers. 

firstNum = 1
nNatural = int(input(" Enter n numbers : "))

print(f'First {nNatural} Natural Numbers:')
while(firstNum <= nNatural):
    print(firstNum)
    firstNum += 1