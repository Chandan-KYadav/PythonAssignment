# Write a python program to create a function that takes a number as a parameter and checks if the number is prime or not. 

def check_prime_not (num):
    
    if num == 1:
        return False
    
    for e in range(2, num):
            if num % e == 0 :
                return False
            
    return True  


# Drive Code

userInput = int(input("Enter a number to check Prime number or not. "))

if check_prime_not(userInput):
    print(" Prime number")
else:
    print("Not a prime number.")
            