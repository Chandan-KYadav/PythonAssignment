# Write a python program to create a function to check whather a numbers falls in a given range. 

def number_in_range (num):
    for e in range(10, 50, 3):
        if num == e:
            return True
        
    return False

num = int(input("Enter a number"))

result = number_in_range(num)

if(result):
    print("Number falls in a given range.")
else:
    print("Number not falls in a given range.")