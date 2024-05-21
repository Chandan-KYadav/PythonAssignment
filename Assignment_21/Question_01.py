# Write a recursive python function to print first N natural numbers. 

def naturalNum(Num):
    if Num > 0:
        naturalNum(Num - 1)
        print(Num,end=" ")
        
# Driver Code 

print("Print First N Natural Numbers:")

userInput = int(input("Enter N numbers: "))

naturalNum(userInput)
    