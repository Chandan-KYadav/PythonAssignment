# Write a python script to check given number is prime number is not. 

num = int(input("Enter a number: "))

while(num > 1):
    for e in range(2,num):
        if(num % e == 0):
            print(f'{num} is Not a Prime Number')
            break
    else:
        print(f'{num} is a prime number')
    
    break
        