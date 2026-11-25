# Methods of set

'''The Union() and update() methods print all items that are present in the two sets.
   The union() method returns a new set whereas update() method adds items into the 
   existing set from another set.''' 

# cities = {"Tokyo", "madrid","berlin","Vapi"}
# citiess = {"Vapi","UP","Maharastra","Vadodara"}
# print(cities.union(citiess))
# cities.update(citiess)


''' The intersection() and Intersection_upate() methods print only items that are similar to both the sets.
    The intersection() method returns a new set whereas intersection_update() methods into the existing set 
    from another set'''
    
# s = {"Tokyo","Madrid","Berlin","Delih"}
# S = {"Tokyo","Seoul","Kabul","Madrid"}
# ss = s.intersection(S)
# ss = s.intersection_update(S)
# print(ss)


'''The difference() and difference_update() methods print only items that are only present in the original set
   and not in both the sets. The difference() methods returns a new set whereas difference_update() method updates
   into the existing set from another set'''
   
# s = {"Tokyo","Madrid","Berlin","Delih"}
# S = {"Tokyo","Seoul","Kabul","Madrid"}
# ss = s.difference_update(S)
# print(ss)


'''from

   There are several methods used for the manipulation of set. They are explained below
   
   isdisjoint(): Disjoint means match nhi hona
   The isdisjoint() method checks if items of given set are present in another set,
   This mehtods return items false if items are present, else it return true'''
   
# s = {"Tokyo","Madrid","Berlin","Delih"}
# S = {"Seoul","Kabul"}
# ss = s.isdisjoint(S)  # items present hoga to false dega or items match nhi hua to true dega
# print(ss)


''' issuperset()
   The issuperset() methods checks if all the items of a particular set are present in the original set
   It returns True if all the items are present, else it return false'''
   
# s = {"Tokyo","Madrid","Berlin","Delih"}
# S = {"Tokyo","Madrid"} #10:22 easy h
# ss = s.issuperset(S)
# print(ss)   


'''issubset
   The issubset() method checks if all the items of the original set are present in the particular set.
   It returns True if all the items are present, else it return false'''
   
# s = {"Tokyo","Madrid"}
# S = {"Tokyo","Seoul","Kabul","Madrid"}  # orginal set k sare items dusre set me present hoge to true verna false (all items )
# ss = s.issubset(S)
# print(ss)


'''add()
   If you want add a single items to the set use the add() method'''
# s = {"Tokyo","Madrid"}
# s.add("India")
# print(s)


'''updates
   If you want to add more than one item, simply create another set or any 
   other iterable object(list,tuple,dictinoary)and use the update() method to 
    add it into existing set'''
    
    
# s = {"Tokyo","Madrid"}
# s.update("India")
# print(s)    


'''remove()/discard()
   We can use remove() and discard() methods to remove items form list'''

# s = {"Tokyo","Madrid"}
# s.remove("Tokyo2")
# s.discard("Tokyo2")
# print(s)   

'''pop()
   This method removes the last of the set but the catch is that we don't know
   which items gets popped as set are unordered. However, you can access the popped
   item if you assign the pop()'''
   

# S = {"Tokyo","Seoul","Kabul","Madrid"} 
# s = S.pop()
# print(S)
# print(s) 


'''del is not a method, rather it is a keyword which deletes the set entirely'''

# S = {"Tokyo","Seoul","Kabul","Madrid"} 
# del S
# print(S)  #output : Error aayga 


'''clear()
   This methods clears all items in the set and print an empty set'''
   
S = {"Tokyo","Seoul","Kabul","Madrid"} 
S.clear()
print(S)
 


