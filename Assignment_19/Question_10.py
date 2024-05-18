# Write a python program to create a function to check wheather a given number is even or odd. 

def even_odd (num):
    if num % 2 == 0 and num > 1:
        print("Number is Even.")
    elif num % 2 != 0 and num > 1:
        print("Number is Odd.")
    else:
        print("Invalid")
        
num = int(input("Enter a number "))

even_odd(num)