# Write a recursive python function to print first N even natural numbers. 

def even_num (num):
    if num > 0 :
        even_num(num - 1)
        if num % 2 == 0:
            print(num, end=" ")
            
# Driver Code 

print("Print first N even natural numbers :")
userInput = int(input("Enter N numbers: "))

even_num(2 * userInput)