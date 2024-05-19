# Write a python program to create a function and print a list where the values are squares of number between 1 and 30. 

def square_of_numbers (firstNum, lastNum):
    l = [e*e for e in range(firstNum,lastNum+1)]
    return l

# Drive Code

FirstValue = 1
LastValue = 30

list_output = square_of_numbers(FirstValue, LastValue)

print(list_output)