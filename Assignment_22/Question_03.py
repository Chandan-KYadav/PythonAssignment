# Write a recursive function to calculate sum of first N even natural numbers. 

def calculate_sum_of_even (firstN):
    if firstN == 0:
        return 0
    
    return ((2 * firstN ) + calculate_sum_of_even(firstN - 1))
        
# Drive Code

print("Calculate Sum of First N Odd Natural number: ")
userInput = int(input("Enter N numbers: "))

result = calculate_sum_of_even(userInput)

print(result)
        