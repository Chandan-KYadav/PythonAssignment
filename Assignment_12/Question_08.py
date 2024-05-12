# Write a python script to print first N terms of fibonacci series. 

num1 = 0
num2 = 1
sum = 0
NthTerm = int(input('Enter N term of Fibonacci series: '))
print(num1)
print(num2)
for e in range(3, NthTerm+1):
    sum = num1 + num2 
    print(sum)
    
    num1 = num2
    num2 = sum 
    
print(f'Sum of {NthTerm} term of fibonacci series is {sum}')