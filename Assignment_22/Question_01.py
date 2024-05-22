# Write a recursive python function to calculate sum of first N natural numbers. 

def calculate_sum_natural (firstN):
    if firstN == 1:
        return 1 
    sum = firstN + calculate_sum_natural(firstN - 1)
    return sum

# Drive Code 

print("Calculate sum of first N natural numbers: ")
userInput = int(input("Enter N numbers: "))

result = calculate_sum_natural(userInput)

print(f'Sum of first {userInput} number is {result}')
        