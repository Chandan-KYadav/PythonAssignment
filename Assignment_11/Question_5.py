#  Write a python script to calculate sum of first N even natural numbers. 

nNumber = int(input('Enter N number: '))
sum = 0 

for e in range(1, nNumber*2):
    if(e % 2 == 0):
        sum = sum + e 
    
print(f'Sum of First {nNumber} Even Natural Number is {sum}')