# Write a python script to print the octal equivalent of a given decimal number. (do not use oct() method)
# 0 1 2 3 4 5 6 7 10 11 12 13 14 15 16 17 20 21 . . . 

decimalNum = int(input('Enter a decimal number: '))
octal = 0
count = 1

while(decimalNum > 0):
    remainder = decimalNum % 8 
    octal += remainder * count
    count *= 10
    
    decimalNum = decimalNum // 8
    
print(f'Octal value 0o{octal}')

