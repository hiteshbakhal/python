'''Exception Handling in Python
   Exception handling is a construct in some programming languages to handle or deal with errors automatically.
   '''
   
'''Python has many built-in exceptions that are raised when your program encounters an error.(something in your program goes wrong)'''

a = input("Enter a number: ")
print(f"multiplication table of {a}  is: ")
try:
    for i in range(1, 11):
        print(f"{a} * {i} = {int(a) * i}")      
except ValueError:
    print("Please enter a valid number")
    
    
    
    
'''imp topic

Syntax :
 try:
    Statements which could generate an exception
    
 except: 
   Soluttion of generated exception'''