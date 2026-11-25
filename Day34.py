# Methods of Dictionary

'''update()
   The update() method updates the value of the key provided to it if the item
   alredy exist in the dictionary, else it creates a new key-value pair'''
   
# info = {'name' : 'Hitesh', 'age': 19,'eligible' : True}
# print(info)
# info.update({'age':21})
# info.update({'DOB':2002})
# print(info)


'''  Clear()
    The clear() method remove all the items from the list or Dictionary'''

# ep1 = {1222:52,123:4846,1684:4684,8974:5464}
# ep2 = {5454:5468,64568:5468,318646:53468,6548:545}
# # ep1.clear()
# empt = {} # This function also clear all the items from dictionary
# print(empt)  

''' The pop() method removes the key-value pair whose key is passed as a parameter'''

# ep1 = {1222:52,123:4846,1684:4684,8974:5464}
# ep2 = {5454:5468,64568:5468,318646:53468,6548:545}

# ep1.pop(1222) 
# print(ep1)

'''popitem()
   The popitem() method removes the last key-value pair from the dictionary.'''
   
# ep1 = {1222:52,123:4846,1684:4684,8974:5464}
# ep2 = {5454:5468,64568:5468,318646:53468,6548:545}

# ep1.popitem()
# print(ep1)


'''del
   we can also use the del keyword to remove a dictionary item'''
   
ep1 = {1222:52,123:4846,1684:4684,8974:5464}
ep2 = {5454:5468,64568:5468,318646:53468,6548:545}

del ep1[1222] # if given value not there in ep1 there program will error

print(ep1)








