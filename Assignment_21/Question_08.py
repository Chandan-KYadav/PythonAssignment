# Write a recursive python function to print cubes of first N natural numbers. 

def cube_of_N_natural (num):
    if num > 0:
        cube_of_N_natural( num - 1)
        
        cube = num * num * num
        print(f'Cube of {num} is {cube}')
        

# Drive Code

print("Print cube of first N natural numbers: ")
userInput = int(input("Enter N numbers: "))

cube_of_N_natural(userInput)