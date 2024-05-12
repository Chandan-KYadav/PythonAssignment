# Write a python script to calculate sum of digit of a given number. 

num = input('Enter a number ')
count = 0
sum = 0
for e in num:
    count = count + 1
    sum = sum + int(e)

print(f'Digit in a {num} is {count} and their sum is {sum}')
