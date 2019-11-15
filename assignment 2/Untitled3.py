#!/usr/bin/env python
# coding: utf-8

# In[8]:


""" Write a program which takes 5 inputs from user for different subject’s
marks, total it and generate mark sheet using grades ? """

sub1=int(input("ENTER FIRST SUBJECT MARKS : "))
sub2=int(input("ENTER SECOND SUBJECT MARKS : "))
sub3=int(input("ENTER THIRD SUBJECT MARKS : "))
sub4=int(input("ENTER FOURTH SUBJECT MARKS : "))
sub5=int(input("ENTER FIFTH SUBJECT MARKS : "))
sub=sub1+sub2+sub3+sub4+sub5
print("total marks:",+sub)
avg=(sub1+sub2+sub3+sub4+sub5)/5
if(avg>=90):
    print("GRADE: A")
elif(avg>=80 and avg<90):
    print("GRADE: B")
elif(avg>=70 and avg<80):
    print("GRADE: C")
elif(avg>=60 and avg<70):
    print("GRADE: D")
else:
    print("GRADE: F")


# In[27]:


""" Write a program which take input from user and identify that the given
number is even or odd? """

user = int(input("ENTER ANY NUMBER AND IDENTIFY THAT THE GIVEN IS EVEN OR ODD : "))
if(user % 2 == 0):
    print("THIS IS A EVEN NUMBER ",+user)
else:
    print("THIS IS A ODD NUMBER ",+user)


# In[29]:


''' Write a program which print the length of the list? '''

ls = ["muaaz","asif","erum"] #STRING
a = len(ls)
print("LENGTH OF THE LIST IS : ", a) 

ls1 = [122,258,85,77,89,55] #NUMERIC
b = len(ls1)
print("LENGTH OF THE LIST IS : ", b) 


# In[30]:


""" Write a Python program to sum all the numeric items in a list? """

ls1 = [122,258,85,77,89,55] #NUMERIC
b = sum(ls1)
print("SUM OF THE LIST IS : ", b) 


# In[34]:


""" Write a Python program to get the largest number from a numeric list. """

ls1 = [122,258,85,77,89,55] #NUMERIC
print("LARGEST NUMBER FROM A NUMBER LIST IS : ",max(ls1))


# In[44]:


"""Take a list, say for example this one:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are
less than 5."""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in a:

    if i < 5:

        print(i)


# In[ ]:




