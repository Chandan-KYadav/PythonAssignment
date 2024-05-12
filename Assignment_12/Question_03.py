# Write a python script to print all prime numbers under 100. 

print('Prime number under 100: ')
for num in range(2, 100):
    for e in range(2, num):
        if(num % e == 0):
            break
    else:
        print(num,end=" ")    