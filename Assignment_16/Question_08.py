# Write a python program to sort a tuples by the second item. tuple1 = (('a',21), ('b',37), ('c',11), ('d',29))

tuple1 =(('a',21), ('b',37), ('c',11), ('d',29))

# using lambda expression
t = tuple(sorted(list(tuple1), key = lambda e : e[1]))

print(t)