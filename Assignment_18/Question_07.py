# Write a python program to create three dictonaries, then create one dictionary that will contain the other three dictonaries. 

dict1 = {"name" : "Chandan"}
dict2 = {"age" : 24}
dict3 = {"gender" : "Male"}

mainDict = {
    "dict1" : dict1,
    "dict2" : dict2,
    "dict3" : dict3
}

print(mainDict)