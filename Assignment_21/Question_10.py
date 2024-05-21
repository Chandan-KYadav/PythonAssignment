# write a recursive python function to print a number in reverse order. 

def num_in_reverse (num):
    if num > 0:
        val1 = num % 10
        print(val1,end="")
    
        num_in_reverse(num // 10)
        
# Derive Code 

num = 1020
num_in_reverse(num)