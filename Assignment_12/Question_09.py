# Write a python script to calculate LCM of two numbers. 

num1 = 10
num2 = 15
greater = 0

# Check greater number 
if(num1 > num2):
    greater = num1
else:
    greater = num2
    
while(1):
    if greater % num1 == 0 and greater % num2 == 0:
        print('LCM is :', greater)
        break
    
    greater += 1