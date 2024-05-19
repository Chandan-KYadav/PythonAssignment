# Write a python program to create a function that takes a list and return a new list with the original list's unique elements. 

def newList (list):
    Uniquelist = []
    i = 0
    while(i < len(list)):
        for e in list:
            if e not in Uniquelist:
                Uniquelist.append(e)
        i += 1
                
    return Uniquelist


list1 = [5, 9, 85, 8, 5, 9, 5]

originalList = newList(list1)

print(originalList)  