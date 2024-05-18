# Write a python program to convert two lists into a dictionary in a way that item from list1 is the key and list2 is the values. 

list1 = ["name", "age", "gender", "location"]
list2 = ["Chandan", 24, "Male", "Faridabad"]

dict1 = {
    list1[0] : list2[0],
    list1[1] : list2[1],
    list1[2] : list2[2],
    list1[3] : list2[3],
}

print(dict1)
