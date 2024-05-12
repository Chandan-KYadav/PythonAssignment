# Write a prime number to print first N prime number. 

nNumber = int(input("Enter N number: "))
count = 1


for e in range(2,nNumber*nNumber):
    for i in range(2,e):
        if e % i == 0:
            break
    else:
        if( count <= nNumber ):
            print(e, end=" ")
            count = count + 1
        else:
            break
        
    

# while(count <= nNumber ):
#     for e in range(2, nNumber*nNumber):
#         for i in range(2, e):
#             if e % i == 0:
#                 break
#         else:
#             print(e, end=" ")
#     count = count + 1