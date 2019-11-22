#!/usr/bin/env python
# coding: utf-8

# In[10]:


'''Make a calculator using Python with addition , subtraction , multiplication ,
division and power.'''

val1 = input("ENTER FIRST VALUE : ")
val2 = input("ENTER FIRST VALUE : ")
operator = input("ENTER OPERATOR : ")
val1 = int(val1)
val2 = int(val2)
if operator == '+':
    val = val1+val2
    print('ANSWER : ',val)
elif operator == '-':
    val = val1-val2
    print('ANSWER : ',val)
elif operator == '*':
    val = val1*val2
    print('ANSWER : ',val)
elif operator == '/':
    val = val1/val2
    print('ANSWER : ',val)
elif operator == '^':
    val = pow(val1,val2)
    print('ANSWER : ',val)
else:
    print("PLEASE ENTER CORRECT OPERATOR ")


# In[6]:


'''Write a program to check if there is any numeric value in list using for loop'''

arr = [1,2,3,4,5,6]
for i in arr:
    if (i == 2):
        print("VALUE IS EXIST")
    else:
        print("VAUE IS NOT EXIST")
        
        
    
    


# In[10]:


'''Write a Python script to add a key to a dictionary'''

customers = {
    'Name':'Muhammad Muaaz',
    'Father Name':'Muhammad Asif',
    'Address':'ABC Road,Karachi'
}
customers['Gender']='Male'
print(customers)


# In[41]:


'''Write a Python program to sum all the numeric items in a dictionary'''

# Python Program to find Sum of Items in a Dictionary
myDict = {'x': 250, 'y':500, 'z':410}
print("Dictionary: ", myDict)
total = 0

# Print Values using get
for i in myDict.values():
    total = total + i
    
print("\nThe Total Sum of Values : ", total)


# In[47]:


'''Write a program to identify duplicate values from list'''

my_list = [20,30,20,30,40,50,15,11,20,40,50,15]
my_list.sort()
for i in range (len (my_list) -1):
     if my_list[i] == my_list[i+1]:
             print (my_list[i])


# In[62]:


'''Write a Python script to check if a given key already exists in a dictionary'''

dic = {
    'a' : 120,
    'b' : 10,
    'c' : 5,
}
if 'b' in dic.keys():
    print(" key already exists")


# In[ ]:




