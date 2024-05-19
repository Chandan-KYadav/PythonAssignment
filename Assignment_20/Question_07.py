# Write a python program to access a function inside a function. 

# For example We create a function for square of a number and add same number in the square. 

def outerFunction (pram):
    
    def innerFunction(pram):
        return pram * pram
    
    return innerFunction(pram) + pram 

# Drive Code 
num = 2

result = outerFunction(num)

print(result)