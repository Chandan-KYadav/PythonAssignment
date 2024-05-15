# Write a python script to print indexies of all occurrence of a given element in a given list. 

givenList = ["Java", "Python", "Javascript", "Reactjs", "SQL"]

for e in givenList:
    indexValue = givenList.index(e)
    
    print(f'{e} has index {indexValue}')
