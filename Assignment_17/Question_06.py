# Write a python program to add elements of list to a set. thisSet = {"Python", "Django", "javascript"} 
# myList = ["Java", "C"]

thisSet = {"Python", "Django", "javascript"}
myList = ["Java", "C"]

# set comprehension
{thisSet.add(e) for e in myList}
print(thisSet)