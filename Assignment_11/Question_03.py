# Write a python script to calculate sum of cube of first N natural number. 

nNumber = int(input('Enter N number: '))
sum = 0 

for e in range(1, nNumber+1):
    square = e**3
    sum = sum + square 
    
print(f'Sum of Square of First {nNumber} Natural Number is {sum}')