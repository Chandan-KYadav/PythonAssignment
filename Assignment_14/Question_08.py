# Write a python script to print distinct elements along with their frequencies of occurance in the list. 

givenList = ["Java", "Python", "Javascript", "Reactjs", "Java", "SQL", "Python"]
emptyList = []

for e in givenList:
     if e not in emptyList:
         valueCount = givenList.count(e)
         
         print(f'{e} have {valueCount} count')
         
         emptyList.append(e)