# Methods of Tuples

# Tuples are immutable, hence if you want to add , remove or chnage tuple items, t
# hence first you must convert the tuples to a list. Then perform operation on that list and convert ot back to tuple

# countries = ("Spain", "china", "India", "Russia")
# temp = list(countries)
# temp.append("London") # use for add item
# temp.pop(3)           # use for remove item
# temp[2] = "Finland"   # use for change item
# countries = tuple(temp)
# print(countries)

# The count() methods of tuple returns the number of items the given element appears in tuple or list.

# o = (0,3,3,6,9,4)
# res = o.count(3)
# print(res)

# The Index() method returns the first occurrence of the given element from the tuple 
  #note :  This methos raise a ValueError if the element is not found in the tuple

# o = (6,1,2,3,4,5,7,8,9)
# res = o.index(6) # 6 kon se no. pe aa rha h vo btata h
# print(res)

# len 

o = (0,3,3,6,9,4)
res = len(o)
print(res)  