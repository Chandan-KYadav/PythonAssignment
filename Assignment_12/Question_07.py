# Write a python scriptto check wheather a given pair of numbers are co-prime numbers or not. 

num1 = 7
num2 = 9

hcf = 1

for e in range(1, num1+1):
    if num1 % e == 0 and num2 % e == 0:
        hcf = e
        
if hcf == 1:
    print('Co-prime No')
else:
    print('Not co-prime no.')