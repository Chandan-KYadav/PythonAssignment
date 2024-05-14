# Write a python program to append elements from another list to the current list ( currentList = ["Java", "Python", "SQL"]
# anotherList = ["C", "Cpp", "NoSQL"])

currentList = ["Java", "Python", "SQL"]
anotherList = ["C", "Cpp", "NoSQL"]

for e in anotherList:
    currentList.append(e)

print(currentList)