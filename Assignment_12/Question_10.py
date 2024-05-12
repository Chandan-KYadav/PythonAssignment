# Write a python script to calculate HCF of two numbers. 

num1 = 10
num2 = 15
greater = 0
LCM = 0
HCF = 0

# Check greater number 
if(num1 > num2):
    greater = num1
else:
    greater = num2
    
while(1):
    if greater % num1 == 0 and greater % num2 == 0:
        LCM = greater
        # print(LCM)
        break
    
    greater += 1
    
multiplyBothNum = num1 * num2

HCF = multiplyBothNum // LCM

print('HCF is :',HCF)