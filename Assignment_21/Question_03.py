# Write a recursive python function to print first N odd natural numbers. 

def odd_num (num):
    if num > 0:
        odd_num(num - 1)
        if num % 2 != 0 :
            print(num, end=" ")
            
# Drive Code 

print("First N Odd Natural Number :")
userInput = int(input("Enter N numbers: "))

odd_num(2 * userInput)