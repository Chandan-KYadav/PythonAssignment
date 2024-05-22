# Write a recursive function to calculate sum of first N odd natural numbers. 

def calculate_sum_of_odd (firstN):
    if firstN == 1:
        return 1
    
    return ((2 * firstN - 1) + calculate_sum_of_odd(firstN - 1))
        
# Drive Code

print("Calculate Sum of First N Odd Natural number: ")
userInput = int(input("Enter N numbers: "))

result = calculate_sum_of_odd(userInput)

print(result)
        