# Write a python script to check whether a given number is positive or non-positive. 

userInput = eval(input('Enter a number '))

if(userInput > 0):
    print(f'{userInput} number is positive')
else:
    print(f'{userInput} number is non-positive')
    