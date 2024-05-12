# Write a python script to calculate factorial of given number. 

num = int(input('Enter a number '))
sum = 0

for e in range(num, 0,-1):
    sum = sum + e
    
print(f'Sum of factorial of  {num} is {sum}')
