# Write a recursive python function to calculate sum of sequares of first N natural numbers. 

def sum_of_squares (firstN):
    if firstN == 1:
        return 1
    
    return firstN * firstN + sum_of_squares(firstN - 1)

# Drive code

print("sum of squares of first N natural numbers: ")
userInput = int(input("enter N numbers: "))

result = sum_of_squares(userInput)

print(result)