# Write a python program to add items from another set to the current set. thisSet = {"Java", "Python", "SQL"} 
# secondSet = {"C", "Cpp", "NoSQL"}

thisSet = {"Java", "Python", "SQL"}
secondSet = {"C", "Cpp", "NoSQL"}

for e in secondSet:
    thisSet.add(e)
    
print(thisSet)