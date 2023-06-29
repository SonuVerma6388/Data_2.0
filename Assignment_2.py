#!/usr/bin/env python
# coding: utf-8

# #  Assignment - 1

# ## Q1. How do you comment code in Python? What are the different types of comments?

# In[1]:


# To do comment in python we can start with "#".
# for example =>

#This is a comment
print("Comment")


# In[2]:


# There are Three  type of comment in python
# 1. Single Line 
# 2. Mulit Line 
# 3.Docstring Comments

# for single line =>
# this is single line comment
print("Singleline Comment")

#for mulit line comment
""" this is a
 multiline comments"""
print("Mulitline Comment")

#for docstring comment
#Python docstring is the string literals with triple quotes that are appeared right after the function.
def multiply(a, b):
    """Multiplies the value of a and b"""
    return a*b
 
 
# Print the docstring of multiply function
print(multiply.__doc__)


# ## Q2. What are variables in Python? How do you declare and assign values to variables?

# In[4]:


# Variables are like container in programing language , which is used to store the value .

# to declare and assign the value in variables =>
a = 10 
b = "Sonu Verma"
c = 1.9
print(a,b,c)


# ## Q3. How do you convert one data type to another in Python?

# In[14]:


# to convert the data type we can do "Explicit Type Conversion"

s = '50'
 
# Converting to int
n = int(s)
print(n)
print(type(n))
 
# Converting to float
f = float(s)
print(f)
print(type(f))


# ## Q4. How do you write and execute a Python script from the command line?

# In[15]:


# To execute a python script from command line  we need to 
# opne command line and type the word python followed by the path to your script file
# for example =>
# python first_script.py
# and press enter to excute


# ## Q5.Given a list my_list = [1, 2, 3, 4, 5], write the code to slice the list and obtain the sub-list            [2, 3].

# In[29]:


# to slice the list 
my_list = [1,2,3,4,5]
print(my_list[1:3])


# ## Q6. What is a complex number in mathematics, and how is it represented in Python?

# In[30]:


# Complex numbers are the numbers that are expressed in the form of a+ib where, 
# a,b are real numbers and 'i' is an imaginary number called “iota”

# to express in python 

a =(2+3j)
print(type(a))


# ## Q7. What is the correct way to declare a variable named age and assign the value 25 to it?

# In[32]:


# the correct waye to declare a variable is 

age = int(25)
print("The age is" ,age)


# ## Q8. Declare a variable named price and assign the value 9.99 to it. What data type does this variable belong to?
# 
# 

# In[33]:


# the type of the variable is "float"

# for example =>
 
price  = 9.99
print(type(price))


# ## Q9. Create a variable named name and assign your full name to it as a string. How would you print the value of this variable?
# 

# In[34]:


name = "Sonu Verma"
print(name)


# ## Q10. Given the string "Hello, World!", extract the substring "World".
# 

# In[43]:


string = "Hello, World!"
    
print(string[7:])

# or

print(string[-6:])


# ## Q11. Create a variable named "is_student" and assign it a boolean value indicating whether you are currently a student or not.
# 

# In[44]:


is_student = True
print(True)


# In[ ]:




