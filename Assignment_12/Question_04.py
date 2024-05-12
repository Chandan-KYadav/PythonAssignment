# Write a python script to print all prime numbers between two given number (both values inclusive)

initialVal = int(input('Enter Initial Value: '))
finalVal = int(input('Enter Final Value: '))

print(f'ALL PRIME NUMBER BETWEEN {initialVal} AND {finalVal}: ')

if(initialVal == 1):
    initialVal = initialVal + 1
    
valRange = range(initialVal, finalVal+1)

for num in valRange:
    for e in range(2, num):
        if num % e == 0:
            break
    else:
        print(num, end=" ")