'''Finally Clause or keyword in Python'''

'''The finally code block is also part of exception handling. When we handle exceptions using try and except blok,
   We can include a finally block at the end . The finally block is always executed, so it is used to doing the concluding
   takss like closing a file resources or database coonections or may be ending the program execution wiht a delightful message to the user.'''
   
  
'''imp''' 
  
'''Syntax:'''
try:
    # Statements which could generate an exception
    pass
except:
    # Solution of generated exception
    pass
finally:
    # This block is always executed 
    #execute in any situation
    pass

try:
  i = [1, 2, 3, 4, 5]
  l = int(input("Enter a number to divide the list elements: "))
  print(i[l])

except:
 print("Please enter a valid number")


finally:
     print("This block is always executed")