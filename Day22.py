#  What is a list in Python?

# list are mutable data types in python. we can add, remove, or change elements in a list after it has been created.
# list are defined using square brackets [] and can contain elements of different data types, including other lists.
# list are ordered collection of data items, meaning that the elements have a specific order and can be accessed using their index.
# The first element in a list has an index of 0, the second element has an index of 1, and so on.
# They store multiple items in a single variable, making it easier to work with large amounts of data.
# Lists are commonly used in Python for tasks such as data analysis, machine learning, and web development.
# List items are separated by commas, and the entire list is enclosed in square brackets. 


l = [1, 2, 3, 4, 5]
hi = ["hi", "hello", "bye"]
print(l)  # Output: [1, 2, 3, 4, 5]
  # Output: ['hi', 'hello', 'bye']
print(type(l))
print(hi)

# Positive indexing starts from 0 and goes up to n-1,
# where n is the number of elements in the list.
# -----
color = ["red", "green", "blue", "yellow", "orange"]
print(color[0])  # Output: red, Positive indexing
print(color[-4])  # Output: orange, Negative indexing 
print(color[5-2])  # Output: green, Positive indexing
# ----

if "voilet" in color:
    print("Yes, 'violet' is in the list.")
else:
    print("No, 'violet' is not in the list.")
    
# ----

if "hel" in "hello":
    print("yes")
    
# -----
# jumped  Index or list slicing     

marks = [85, 92, 78, 96, 88, 90, 75, 89, 95, 82]
print(marks)
print(marks[0:8:2])  # start, stop, step formula


# -------

# list comprehension are used for creating new lists from existing iterables like lists, tuples, or strings, sets and dictionaries. and even in arrays.

lst = [i**i for i in range(4)]
print(lst)  
lst = [i for i in range(1000) if i%2==0]
print(lst)  #ye line define krti h ki jo bhi range dege vo 2 divible hogi ya nhi