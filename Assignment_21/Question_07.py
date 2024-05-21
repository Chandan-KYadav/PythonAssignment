# Write a recursive python function to print squares of first N natural numbers. 

def square_of_N_natural (num):
    if num > 0:
        square_of_N_natural( num - 1)
        
        square = num * num 
        print(f'Square of {num} is {square}')
        

# Drive Code

print("Print square of first N natural numbers: ")
userInput = int(input("Enter N numbers: "))

square_of_N_natural(userInput)