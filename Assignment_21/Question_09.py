# Write a recursive python function to print first N multiples of a given number. 

def find_multiples (num,N):
    if N > 0:
        find_multiples(num, N-1)
        multiple = num * N 
        print(f'{num} X {N} = {multiple}')
    
# Drive Code 

print("Print first N multiples of given number: ")
userInput = int(input("Enter number: "))
givenNum = 5

find_multiples(givenNum,userInput)