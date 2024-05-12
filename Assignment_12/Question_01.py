# Write a python script to reverse a number. 


num = 9090
 
while(num > 0):
    value = num % 10
    print(value,end="")
    
    num = num // 10
    