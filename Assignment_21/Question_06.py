# Write a recursive python function to print first N even natural numbers in reverse order. 

def even_num_reverse (num):
    if num > 0 :
        if num % 2 == 0:
            print(num, end=" ")
        even_num_reverse(num - 1)
        
            
# Driver Code 

print("Print first N even natural numbers in reverse order :")
userInput = int(input("Enter N numbers: "))

even_num_reverse(2 * userInput)