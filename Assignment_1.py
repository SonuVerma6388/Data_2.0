#!/usr/bin/env python
# coding: utf-8

# # Assignment - 1

# ### Q1. Create one variable containing following type of data.
#         1) string
#         2) list
#         3) float
#         4) tuple

# In[1]:


# to make this type of variable be can make through list, set, tuple, & Dictionary.

var = ["sonu", [1,2,3,4], 2.0, ("apple", "mango", "banana")]
print(var)


# ### Q2. Given are some following variables containing data:
#     1) var1 = ‘ ‘
#     2) var2 = ‘[ DS , ML , Python]’
#     3) var3 = [ ‘DS’ , ’ML’ , ‘Python’ ]
#     4) var4 = 1.
# ### What will be the data type of the above given variable.

# In[2]:


# to find the data type of variable be can use type() function

var1 = ''
type(var1)


# In[3]:


var2 = '[ DS , ML , Python]'
type(var2)


# In[4]:


var3 = [ 'DS' , "ML" , "Python" ]
type(var3)


# In[5]:


var4 = 1.
type(var4)


# ### Q3.  Explain the use of the following operators using an example:
#         1)/
#         2)%
#         3)//
#         4)**

# In[6]:


# '/' this operator Divides the number on its left by the number on its right and returns a floating point value. .
# for example -

x = 10
y = 5
print(x/y)


# In[7]:


# '%' this operator is use to find Modulus in python
# for example -
x =10
y = 5
print(x%y)


# In[8]:


# '//' This operator will divide the first argument by the second and round the result down to the nearest whole number,
# making it equivalent to the math.
# for example -

x = 13
y = 3
print(x//y)


# In[9]:


# '**' this is one of the Arithmetic Operator which is use for to calculate Exponentiation 
# for example - 
x = 2 
y = 3

c = x**y
print(c)


# ### Q4. Create a list of length 10 of your choice containing multiple types of data. Using for loop print the element and its data type.

# In[10]:


list = ["sonu", 63, 2.5, ("a","b", 'c')]
for i in list:
    print(i, "=", type(i))


# ### Q5. Using a while loop, verify if the number A is purely divisible by number B and if so then how many times it can be divisible.

# In[ ]:


# I can't understand the question .


# ### Q6. Create a list containing 25 int type data. Using for loop and if-else condition print if the element is divisible by 3 or not.

# In[11]:


list = []
for i in range(0,25):
    list.append(i)
print(list)
        


# In[12]:


for i in list:
       if i%3 == 0:
           print(i,"is divisible by 3.")
       else :
           print(i,"is  not divisible by 3.")


# ### Q7. What do you understand about mutable and immutable data types? Give examples for both showing this property.

# In[13]:


# Mutable 

# A mutable object can be changed after it is created.
# Mutable Objects are of type list, dict, or set. Custom classes are generally mutable. 

# for examples =>

pen = ["red_pen", "blue_pen", "green_pen"]
print(pen)
 
pen[0] = "pink_pen"
pen[-1] = "orange_pen"
print(pen)


# In[14]:


# Immutable
# An immutable object can’t be changed after it is created.
# Immutable Objects are of in-built datatypes like int, float, bool, string, Unicode, and tuple.  

# for example =>

tuple1 = (0, 1, 2, 3)
tuple1[0] = 4
print(tuple1)


# In[ ]:





# In[ ]:




