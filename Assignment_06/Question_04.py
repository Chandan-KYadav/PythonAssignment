# Write a python script to print greater between two numbers .Print numbers only once even if the numbers are the same. 

num1 = int(input('Enter Number One '))
num2 = int(input('Enter Number Two '))

if(num1 > num2):
    print(f'{num1} is greater than {num2}')
elif(num1 == num2):
    print(f'Both are equal numbers.')
else:
    print(f'{num2} is greater')