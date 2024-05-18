# Write a python program to create a dictionary that contains three dictionaries(nested). 

dict1 = {
    "person1" : {
    "name" : "Chandan", 
    "age" : 24,
    "gender" : "Male", 
    "location" : "Faridabad", 
    "qualification" : {
        "degree" : "B.Tech",
        "trade" : "Electrical"
    }
    },
    
    
    "person2" : {
    "name" : "Virender", 
    "age" : 34,
    "gender" : "Male", 
    "location" : "Faridabad", 
    "qualification" : {
        "degree" : "B.Tech",
        "trade" : "Electronics"
    }
    }
}

print(dict1)