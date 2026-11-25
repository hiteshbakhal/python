#  for  loop with else in python

'''Python allows the else keyword to be used with the for loop and while loops too
   The else block appears after the body of the loop. The statement in the else block
    will be executed after all iteration are completed. The program exit the loop only 
    after the else block is executed'''
 
'''Imp'''   
    
# for i in range(5):
#     print(i)
#     if i == 4:
#         break
# else:
#     print("Sorry no i")
    
    
for x in range(5):
    print ("iteration no {} in for loop".format(x+1))
else:
    print("else")
    print("out")       
    
    