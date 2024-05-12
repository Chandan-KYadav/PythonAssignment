# Write a python script to calculate sum of first N natural numbers. 

nNumber = int(input('Enter N number: '))
sum = 0 

for e in range(1, nNumber+1):
    sum = sum + e 
    
print(f'Sum of First {nNumber} Natural Number is {sum}')