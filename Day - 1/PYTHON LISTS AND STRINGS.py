#!/usr/bin/env python
# coding: utf-8

# There are four collection data types in the Python programming language:
 
# List is a collection which is ordered and changeable. Allows duplicate members.
 
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
 
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

# LISTS 

# Lists are used to store multiple items in a single variable.
 
# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
 
# Lists are created using square brackets.

# Their usage and some functions are shown below with examples:
 


example = ["Sunday", "Monday", "Tuesday", "Wednesday"]
print(example)


# type()
 
# From Python's perspective, lists are defined as objects with the data type 'list':

mylist = ["apple", "banana", "cherry"]
print(type(mylist))



# The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.
# 
# Accessing elements in a List:
# Accessing elements in a list basically means getting the value of an element at
# some arbitrary index in the list.
# Indexes are assigned on 0 based basis in python. We can also access elements in
# python with negative indexes. Negative indexes represent elements, counted
# from the back (end) of the list.



example = ["Sunday", "Monday", "Tuesday", "Wednesday"]

# Positive Indexing
print(example[0], example[1])



# Negative Indexing
print(example[-1])


# Slicing a List:
#     
# Slicing is the process of accessing a part or subset of a given list.


example = ["Sunday", "Monday", "Tuesday", "Wednesday"]

# Positive Slicing
print(example[0:2])


# Negative Slicing
print(example[-3:-1])



# Changing Values in a List:
# We can change values at some particular index in a list by accessing the element
# with [] and then setting it to some other value

example = ["Sunday", "Monday", "Tuesday", "Wednesday"]
print(example)


example[0] = "Saturday"
print(example)



# List Concatenation and Replication:
# When we merge the contents of 2 lists into one list, it is called list concatenation.


example = ["Sunday", "Monday", "Tuesday", "Wednesday"];
example1 = ["Weekdays", "Weekends"]

# Concatenation
example = example + example1
print(example)



# Copying the contents of a list, some finite number of times into the same or some list
# is called list replication.
# 



example = ["Sunday", "Monday", "Tuesday", "Wednesday"];
example1 = ["Weekdays", "Weekends"]
# Replication
example1 = example1 * 3
print(example1)




# Delete values from Lists:
# We can delete a particular element from a list by using the del keyword


example = ["Sunday", "Monday", "Tuesday", "Wednesday"];
print(example)
del example[2]
print(example)



# Looping through Lists:
# The below example shows how we can iterate over all the elements present in a
# list.

example = ["Sunday", "Monday", "Tuesday", "Wednesday"]
for ex in example:
    print(ex)



# in and not in keywords:
# With the in keyword, we can check if some particular element is present in the given
# python variable.
# Similar to the not in keyword, we can check if some particular element is not present
# in the given python variable.
# 


example = ["Sunday", "Monday", "Tuesday", "Wednesday"]
print("Sunday" in example)
print("Hello" not in example)


# List Methods
# 
# Python has a set of built-in methods that you can use on lists.
# 
# Method	    Description
# 
# append()	Adds an element at the end of the list
# 
# clear()	Removes all the elements from the list
# 
# copy()	Returns a copy of the list
# 
# count()	Returns the number of elements with the specified value
# 
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# 
# index()	Returns the index of the first element with the specified value
# 
# insert()	Adds an element at the specified position
# 
# pop()	Removes the element at the specified position
# 
# remove()	Removes the item with the specified value
# 
# reverse()	Reverses the order of the list
# 
# sort()	Sorts the list
# 
# 


# Adding Values in Lists:
# insert(): This function inserts an element into a particular index of a list.


example = ["Sunday", "Monday", "Tuesday", "Wednesday"]
print(example)
example.insert(1, 'Days')
print(example)



# append(): This function appends an element at the back of a list.
# 


example = ["Sunday", "Monday", "Tuesday", "Wednesday"]
print(example)
example.append('Days')
print(example)



# Sorting a List:
# Sorting a list means arranging the elements of the list in some particular order.
# We sort a list by using the sort() function.


# Sorts in lexicographical order
example = ["Sunday", "Monday", "Tuesday", "Wednesday"];
print(example)
# Sort in ascending order
example.sort()
print(example)
# Sort in descending order
example.sort(reverse = True)
print(example)
example = [1, 5, 3, 7, 2]
# Sort in ascending order
example.sort()
print(example)
# Sort in descending order
example.sort(reverse = True)
print(example)


#List Length

thislist = ["apple", "banana", "cherry"]
print(len(thislist))



#pop() method

thislist = ["apple", "banana", "cherry"]
print(thislist.pop(1))
print(thislist)


#reverse() method

thislist = ["apple", "banana", "cherry"]
print(thislist.reverse())
print(thislist)



# # STRINGS

# Strings in python are surrounded by either single quotation marks, or double quotation marks.
# 
# 'hello' is the same as "hello".
# 
# You can display a string literal with the print() function:



print('hello')
print("hello")



# Multiline Strings:
#     
# Multiline Strings are used in python through triple quotes '''
# 
# Example:
# 


a = ''' Hello
World!
This is a
Multiline String.'''
print(a)



# Strings Indexing:
#     
# Strings in Python are indexed the same way as a list of characters, based on 0-based
# indexing. We can access elements of a string at some index by using the [] operators.


a = "Python"
print(a[0], a[2], a[4])
print(a[-1], a[-3], a[-5])


# In[ ]:





# Strings Slicing:
# 
# Slicing is also done the same way as in lists.
# 

# In[3]:


a = "Hello"
# Slices the string from 0 to 3 indexes
print(a[0:3])
# Slices the string from 3 to -1(same as 4) indexes
print(a[3:-1])


# In[ ]:





# # String Methods
# 
# Method	Description
# 
# capitalize()	Converts the first character to upper case
# 
# casefold()	Converts string into lower case
# 
# center()	Returns a centered string
# 
# count()	Returns the number of times a specified value occurs in a string
# 
# encode()	Returns an encoded version of the string
# 
# endswith()	Returns true if the string ends with the specified value
# 
# expandtabs()	Sets the tab size of the string
# 
# find()	Searches the string for a specified value and returns the position of where it was found
# 
# format()	Formats specified values in a string
# 
# format_map()	Formats specified values in a string
# 
# index()	Searches the string for a specified value and returns the position of where it was found
# 
# isalnum()	Returns True if all characters in the string are alphanumeric
# 
# isalpha()	Returns True if all characters in the string are in the alphabet
# 
# isdecimal()	Returns True if all characters in the string are decimals
# 
# isdigit()	Returns True if all characters in the string are digits
# 
# isidentifier()	Returns True if the string is an identifier
# 
# islower()	Returns True if all characters in the string are lower case
# 
# isnumeric()	Returns True if all characters in the string are numeric
# 
# isprintable()	Returns True if all characters in the string are printable
# 
# isspace()	Returns True if all characters in the string are whitespaces
# 
# istitle()	Returns True if the string follows the rules of a title
# 
# isupper()	Returns True if all characters in the string are upper case
# 
# join()	Joins the elements of an iterable to the end of the string
# 
# ljust()	Returns a left justified version of the string
# 
# lower()	Converts a string into lower case
# 
# lstrip()	Returns a left trim version of the string
# 
# maketrans()	Returns a translation table to be used in translations
# 
# partition()	Returns a tuple where the string is parted into three parts
# 
# replace()	Returns a string where a specified value is replaced with a specified value
# 
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# 
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# 
# rjust()	Returns a right justified version of the string
# 
# rpartition()	Returns a tuple where the string is parted into three parts
# 
# rsplit()	Splits the string at the specified separator, and returns a list
# 
# rstrip()	Returns a right trim version of the string
# 
# split()	Splits the string at the specified separator, and returns a list
# 
# splitlines()	Splits the string at line breaks and returns a list
# 
# startswith()	Returns true if the string starts with the specified value
# 
# strip()	Returns a trimmed version of the string
# 
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# 
# title()	Converts the first character of each word to upper case
# 
# translate()	Returns a translated string
# 
# upper()	Converts a string into upper case
# 
# zfill()	Fills the string with a specified number of 0 values at the beginning

# In[ ]:





# Case Conversion Functions:
# 
# The upper() and lower() functions are used to convert a string of letters into
# uppercase or lowercase respectively.
# 
# The isupper() and islower() functions are used to check if a string is in all uppercase or
# lowercase respectively.

# In[4]:


a = "Hello"
print(a)
#Converts string to uppercase
print(a.upper())
# Converts string to lowercase
print(a.lower())
# Checks if string is uppercase
print(a.isupper())
# Checks if string is lowercase
print(a.islower())


# In[ ]:





# Function Explanation
# 
# isspace()
# Returns True if all characters in string are
# whitespaces
# 
# isalnum() Returns True if given string is alphanumeric
# 
# isalpha() Returns True if given character is alphabet
# isTitle()
# 
# Returns True if string starts with an uppercase
# letter and then rest of the characters are
# lowercase

# In[ ]:





# join() and split() Functions:
#     
# join() function merges elements of a list with some delimiter string, and returns the
# result as a string.
# 

# In[5]:


list = ["One", "Two", "Three"]
# join function
s = ','.join(list)
print(s)


# In[ ]:





# split() function splits the into tokens, based on some delimiters and returns the result
# as a list

# In[6]:


# split function
newList = s.split(',')
print(newList)


# In general, a string can be split to list using split() method and a list can be joined to
# string using the join() method 

# In[ ]:





# String Formatting:
# String Formatting is done with the str.format() function.

# In[9]:


first = "first"
second = "second"
s = "Sunday is the {} day of the week, whereas Monday is the {} day of the week".format
print(s)


# In[ ]:





# String Length
# To get the length of a string, use the len() function.

# In[10]:


a = "Hello, World!"
print(len(a))


# In[ ]:




