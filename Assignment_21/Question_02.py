# Write a recursive python function to print first N natural numbers in reverse order. 

def natural_reverse (num):
    if num > 0 :
        print(num, end=" ")
        natural_reverse(num - 1)
        
# Drive Code 

print("Print first N natural numbers in reverse order:")
userInput = int(input("Enter N numbers: "))

natural_reverse(userInput)