# Write a recursive python script to print first N odd natural numbers in reverse order. 

def odd_num_reverse (num):
    if num > 0:
        if num % 2 != 0 :
            print(num, end=" ")
        odd_num_reverse(num - 1)
        
            
# Drive Code 

print("First N Odd Natural Number :")
userInput = int(input("Enter N numbers: "))

odd_num_reverse(2 * userInput)