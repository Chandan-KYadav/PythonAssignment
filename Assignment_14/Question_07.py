# Write a python script to remove all non int valves from a list. 

givenList = ["Java", 1 , "Python", 5.2, "Javascript", 9.5, 2.1]

newList = []

for e in givenList:
    if type(e) != float :
        newList.append(e)
        
print(newList)
