# What is Sets {}

''' Sets are unordered collection of data items. They store multiple items in a single varible. 
    set items are separated by commas and enclosed within curly brackets{}.
    Sets are unchangeble, meaning you cannot change items of the set once created.sets do not contain duplicate items'''
    
s =  {3,5,4,3}
print(s)

info = {"carla",19,False,19,9.5}
print(info)

#  empty set create krna h to set() kr k krna 
#  if h = {} kr k krega to return me dict return krega 
hn = set()
print(hn,type(hn))

for value in info:
    print(value)