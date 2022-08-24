#!/usr/bin/env python
# coding: utf-8

# ## $$Conditional\ statements $$

# # Introducing Indentation

# <li>In simple terms indentation refers to adding white space before a statement</li>
# <li>Indentation is a very important concept of Python because without proper indenting the Python code, you will end up seeing IndentationError and the code will not get compiled.</li>



# what happens when we dont give indentation.
num = True

if(num):
print('successful')

print('This line will print always')


# ## if Statement

# <img src = '1.jpg'>

# In[2]:


# we are checking the condition by giving True. if we give false or o or None the condition fails
num = True

if(num):
    print('Number is positive')

print('This line will print always')


# #### taking the input from user

# In[4]:


# give a numerical number.
num = int(input())
if num > 0:
    print("{} is positive.".format(num))


# In[5]:


# if condition in strings
string = "abcdef"
if string.islower():
    print(string.upper())


# In[9]:


num = int(input())

if num > 8:
    print("condition1")
if num < 10:
    print("condition2")


# ### Nested if statement

# In[2]:


num = 8
if num >= 0:
    if num == 0:
        print("zero")
    else:
        print("Positive number")
else:
    print("Negative number")


# ## if.....else Statement

# <img src = '2.jpg'>

# In[6]:


# if - else statement on numerical values. 
num = -1

if(num >= 0):
    print('Positive')
else:
    print('Negative')
print('This line will print anyways')


# In[7]:


string = "python123"

if string.isalnum():
    print("yes")


# ### checking if condition with operators

# In[8]:


# checking the number with operators.
num = int(input())

if num > 0 and num < 9:
    print("{} is a single digit".format(num))
else:
    print("{} is not a single digit".format(num))


# ## if......elif......else Statement

# <img src = '3.jpg'>

# In[9]:


# if - else - elif statement
num = int(input())

if(num > 0):
    print('{} is Positive'.format(num))
elif(num == 0):
    print('ZERO')
else:
    print('{} is Negative'.format(num))


# In[10]:


# Try 90, 78, 50, 9999

grade = int(input())

if grade >= 90 and grade<=100:
    print("A grade")

elif grade >=80 and grade<=90:
    print("B grade")

elif grade >=70:
    print("C grade")

elif grade >= 65:
    print("D grade")

else:
    print("Failing grade")


# ## Nested if - else Statements

# In[11]:


num = 0

if num >= 0:
    if num == 0:
        print('Zero')
    else:
        print('Positive')
else:
    print('Negative')


# In[12]:


# Try 90, 78, 50, 9999

grade = int(input())

if grade <= 100:

    if grade >= 90 and grade<=100:
        print("A grade")

    elif grade >=80 and grade<=90:
        print("B grade")

    elif grade >=70:
        print("C grade")

    elif grade >= 65:
        print("D grade")

    else:
        print("Failing grade")
else:
    print("Enter a value below 100 and greater than 0")


# In[13]:


grade = int(input())

if grade >= 65 and grade<=100:
    print("Passing grade of:", end = ' ')

    if grade >= 90:
        print("A")

    elif grade >=80:
        print("B")

    elif grade >=70:
        print("C")

    elif grade >= 65:
        print("D")

elif grade>100:
    print('Enter a value less than 100')
        
else:
    print("Failing grade")


# In[ ]:




