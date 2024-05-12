# Write a python script to find next prime number of a given number. 

num = int(input('Enter number to find next prime number :'))

while(num > 1):
    for e in range(2, num):
        if num % e == 0:
            num = num + 1
            break
    else:
        print(num)
        break