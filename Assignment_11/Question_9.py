# Write a python script to print binary equivalent of a given decimal number.(do not use bin() method)

# 128 64 32 16 8 4 2 1

userValue = int(input('Enter a number: '))
binary = ""
num = userValue
while(num > 0):
    binary = str(num % 2) + binary
    
    num = num // 2
    
print(f'Binary of {userValue} is 0b{binary}')
