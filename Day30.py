# What is Recursion?

""" Recursion is a programming tachnique where a function calls itself to
    solve a larger problem by breaking it down into smaller, manageable sub-problems"""
    
'''Three Golden Rules

1. self-calling : The function repeats the exact same logic by calling itself
2. Smaller input : Each call works on a smaller or simpler version of the problem
3. The Base Case : A mandatory stop-condition that prevents the function from calling 
    itself forever(avoiding a crash/stack overflow)'''
    
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)


num = 8;
print("number", num)
print("factorial",factorial(num))


# Fibonacci Series

'''
f0 = 0
f1 = 1
f2 = f1 + f0
fn = f(n-1) + f(n+2)'''




