# Methods of list

l = [5,9,67,34,23,45]
print(l)
l.append(2) # last me koi bhi element add krne ke liye append method use hota h
print(l)



l = [5,9,67,34,23,45]
print(l)
l.sort() # sort method is used to sort the list in ascending order
print(l)    

l = [5,9,67,34,23,45]
print(l)
l.sort(reverse=True) # sort method is used to sort the list in descending order
print(l) 


l = [5,9,67,34,23,45]
print(l)
l.reverse() # reverse method is used to reverse the list
print(l) 


l = [5,9,67,34,23,45]
print(l)
print(l.index(67)) # index method is used to find the index of an element in the list and return first occurence 

l = [5,9,67,34,23,45]
print(l)
print(l.count(67)) #count krta h ki 67 kitni bar aaya h     



l = [5,9,67,34,23,45]
print(l)
m = l.copy() #copy method
m[0] = 0
print(l)


l = [5,9,67,34,23,45]
print(l)
l.insert(1,63) #insert methos use for koi bhi no. add kr skte h kisi bhi place pe 
print(l)


l = [5,9,67,34,23,45]
print(l)
m = [800,900,100]
l.extend(m) # extend() method use for add one list to another list  
# k = l + m 
# print(k) you can write like this also to run code
print(l)