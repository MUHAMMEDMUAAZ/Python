#!/usr/bin/env python
# coding: utf-8

# In[2]:


"""Write a Python function to calculate the factorial of a number (a non-negative
integer). The function accepts the number as an argument.
"""

def factorial(n):
    if n == 0:
        return 1
    elif n<0:S
        print("PLEASE ENTER NUMBER NON-NEGATIVE INTEGER")
    else:
        return n * factorial(n-1)
n=int(input("Input a number to compute the factiorial : "))
print(factorial(n))


# In[3]:


"""Write a Python function that accepts a string and calculate the number of upper
case letters and lower case letters.
"""


def check_upper_lower(user):
    count1 = 0  
    count2 = 0
    for use in user:
        if(use.islower()):
            count1=count1+1
        elif(use.isupper()):
            count2=count2+1
        else:
            print("")
    print ("Original String : ", user)
    print("The number of lowercase characters is:",+count1)
    print("The number of uppercase characters is:",+count2)
    
check_upper_lower('PAkistan')


# In[4]:


"""Write a Python function to print the even numbers from a given list."""


def is_even_num(l):
    enum = []
    for n in l:
        if n % 2 == 0:
            enum.append(n)
    return enum
print(is_even_num([1, 2, 3, 4, 5, 6, 7, 8, 9]))
 


# In[5]:


"""Write a Python function that checks whether a passed string is palindrome or not.
Note: A palindrome is a word, phrase, or sequence that reads the same
backward as forward, e.g., madam"""


def isPalindrome(string):
    left_pos = 0
    right_pos = len(string) - 1
    while right_pos >= left_pos:
        if not string[left_pos] == string[right_pos]:
            return  'string is not palindrome'
        left_pos += 1
        right_pos -= 1
    return  'string is palindrome'
print(isPalindrome('madam')) 


# In[37]:


"""Write a Python function that takes a number as a parameter and check the
number is prime or not"""


def test_prime(n):
    if (n==1):
        return 'It is not prime number'
    elif (n==2):
        return 'It is prime number';
    else:
        for x in range(2,n):
            if(n % x==0):
                return 'It is not prime number'
        return 'It is prime number'
n = int(input("Enter any number to check prime or not ::: "))
print(test_prime(n))


# In[35]:


"""Suppose a customer is shopping in a market and you need to print all the items
which user bought from market.
Write a function which accepts the multiple arguments of user shopping list and
print all the items which user bought from market.
(Hint: Arbitrary Argument concept can make this task ease)"""


def list(a,b,c,d,e,f):
    print("We bought " +a + " from market")
    print("We bought " +b + " from market")
    print("We bought " +c + " from market")
    print("We bought " +d + " from market")
    print("We bought " +e + " from market")
    print("We bought " +f + " from market")
    
list("Rice","Sugar","Egg","Bread","Medicines","Toys")




# In[ ]:





# In[ ]:




