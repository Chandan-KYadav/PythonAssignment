# Write a python script which takes a three digit number from the user and displays only its midle digit. 

userInput = int(input('Enter three digit number'))

# Calculation

# Two digit 

middleDigit = userInput // 10

# Middle digit

middleDigit = middleDigit % 10

# Result 

print(f'Output is {middleDigit}')