# Write a python program to check if all the items in the tuple are the same. 

tuple1 = ("Java", "Python", "Javascript", "SQL")
count = 0
flag = 1

while count < len(tuple1):
    for e in tuple1:
        if tuple1[count] == e:
            flag += 1
            
    count += 1
            
if flag == len(tuple1):
    print("All items are same in tuple.")
else:
    print("All items are not same in tuple")