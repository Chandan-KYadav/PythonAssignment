# Write a python program to print all key names in the dictionary one by one. 

dict1 = {"name" : "Chandan", "age" : 24, "gender" : "Male", "location" : "Faridabad", "qualification" : "B.Tech"}

list_of_keys = dict1.keys()

for e in list_of_keys:
    print(e)