# Write a pthon program to copy element 4 and 5 from the following tuple into new tuple. tuple1 = (1, 2, 3, 4, 5, 6)

tuple1 = (1, 2, 3, 4, 5, 6)
list_empty = []
count = 0

for e in tuple1:
    if count == 3 or count == 4:
        list_empty.append(e)
    count += 1
    
newTuple = tuple(list_empty)
print(newTuple)