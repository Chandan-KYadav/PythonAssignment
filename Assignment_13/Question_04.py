# Write a python script to change the values "SQL" and "Reactnative" with the values "NOSQL" and "Flutter" (List is theList = ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"])

theList = ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]

for e in theList:
    
    if e == "SQL":
        theList[theList.index("SQL")] = "NOSQL"
    elif e == "Reactnative" :
        theList[theList.index("Reactnative")] = "Flutter"
           
print(theList)