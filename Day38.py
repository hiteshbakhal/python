'''Custom Erros 

   In python , we can raise custom erros by using the raise keyword'''
   
   
'''imp topic   search on google Erros classes'''

   
hu = int(input("Enter your salary: "))

if (hu<5 or hu>9):
    raise ValueError("Salary should be between 5 and 9 lakhs")