#   What is a function in Python?

#  A function is a self-contained block of code that performs a specific task.
# Functions are used to organize code into reusable pieces, making it easier to read,
# maintain, and debug. In Python, functions are defined using the `def` keyword,
# followed by the function name and parentheses that may include parameters.


# --------
# There are two types of functions in Python: built-in functions and user-defined functions.
# ---------


# There are four types of arguments that can be passed to a function in Python:

# {  Deafault arguments are parameters that have a default value assigned to them in the function definition.
# If the caller does not provide a value for that parameter, the default value will be used. 
# This allows for more flexible function calls and can help reduce the number of required arguments.}

# { Keyword arguments are passed to a function by explicitly specifying the parameter name and its corresponding value.
# This allows for more flexibility in the order of arguments and makes the code more readable.}

# { Variable-length arguments allow a function to accept an arbitrary number of arguments.
# In Python, this is achieved using the *args syntax for positional arguments and **kwargs syntax for keyword arguments.}

#{ Required arguments are the most common type of arguments in Python functions.
# They are the parameters that must be provided when calling a function, and they are defined in the function's signature.
# If a required argument is not provided, Python will raise a TypeError.}


# Deafult arguments 
def name(Hname, Iname="Ashok",Tname="Das"):
    print("Hello,",Hname,Iname,Tname)
    
name("Rahul")  # Output: Hello Rahul Ashok Das

# Keyword arguments easy hai koi bhi order me pass kar sakte ho or kese bhi likh skte ho visa versa:

# Required arguments me tuje argumets pass krni hi hogi nhi krega to error aayga 


