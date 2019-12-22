#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""Question 1:
Define Object Oriented Programming Language?"""


# ANSWER


"""One of the popular approach to solve a programming problem is
by creating objects. This is known as Object-Oriented Programming (OOP)."""



# In[2]:


"""Question 2:
List down the Benefits of OOP?"""


# ANSWER


"""
1. Modularity for easier troubleshooting
2. Reuse of code through inheritance
3. Flexibility through polymorphism
4. Effective problem solving
"""

""" OR """


"""
·        Through inheritance, we can eliminate redundant code and extend the use of existing classes.

·        We can built programs from standard working modules that communicate with one another rather than, having to start writing the code from scratch. This leads to saving of development time and higher productivity.

·        The principle of data hiding helps the programmers to built secure program that can’t be invaded by code in other parts of the program.

·        It is possible to have multiple objects to coexist without any interference.

·        It is possible to map objects in the problem domain to those objects in the program.

·        It is easy to partition the work in a project based on objects.

·        The data-centered design approach enables us to capture more details of the model in an implementable form.

·        Object-oriented systems can be easily upgraded from small to large system

·        Message passing technique for communication between objects make the interface descriptions with external system much simpler.

·        Software complexity can be easily managed.

 
"""


# In[3]:


"""Question 3:
Differentiate between function and method?"""

# ANSWER

"""
As we get the basic understanding of the function and method both, let's highlight the key differences between them −

Unlike a function, methods are called on an object. Like in our example above we call our method .i.e. “my_method” on the object “cat” whereas the function “sum” is called without any object. Also, because the method is called on an object, it can access that data within it.

Unlike method which can alter the object’s state, python function doesn’t do this and normally operates on it.

In Short, a method is a function which belongs to an object.
"""


# In[1]:


"""
Question 4:
Define the following terms:
1. Class
2. Object
3. Attribute
4. Behavior
"""

# ANSWER

# CLASS

"""The class can be defined as a collection of objects. It is a logical entity that has some specific attributes and methods.
For example: if you have an employee class then it should contain an attribute and method, i.e. an email id, name, age, salary, etc."""


# OBJECT

"""The object is an entity that has state and behavior. It may be any real-world object like the mouse, keyboard, chair, table, pen, etc.
Everything in Python is an object, and almost everything has attributes and methods. All functions have a built-in attribute __doc__, which 
returns the doc string defined in the function source code."""


# ATTRIBUTE

"""Everything in Python is an object, and almost everything has attributes and methods. In python, functions too are objects. So they have attributes like other objects. All functions have a built-in attribute __doc__, which returns the doc string defined in the function source code.
We can also assign new attributes to them, as well as retrieve the values of those attributes"""

# BEHAVIOR

"""Behaviour of any object is equivalent to the functions that it can perform. In OOP it is possible to assign some functions to objects of a class. Taking the example forward, like a student can read/write, the car can accelerate and so on."""


# In[32]:


"""
Question 5:
Write a code in python in which create a class named it Car which
have 5 attributes such like (model, color and name etc.) and 3
methods. And create 5 object instance from that class.
"""

class car():
    def __init__ (self,model,color,name,speed,door):
        self.model=model
        self.color=color
        self.name=name
        self.speed=speed
        self.door=door
        
    def updatecolor(self,newcolor):
        self.color=newcolor
    def updatespeed(self,newspeed):
        self.speed=newspeed
    def updatedoor(self,newdoor):
        self.door=newdoor
print("-------------------------------------------- \n                    car1\n--------------------------------------------")
car1=car("2001","black","toyota","335km/h","4")
print("MODEL "+car1.model)
print("COLOR "+car1.color)
print("NAME "+car1.name)
print("SPEED "+car1.speed)
print("DOOR "+car1.door)

car1.updatecolor("UPDATE COLOR "+"Red")
print(car1.color)

car1.updatespeed("UPDATE SPEED "+"445km/h")
print(car1.speed)

car1.updatedoor("UPDATE DOOR "+"5")
print(car1.door)


print("-------------------------------------------- \n                    car2\n--------------------------------------------")
car2=car("2002","white","corolla","455km/h","4")
print("MODEL "+car1.model)
print("COLOR "+car1.color)
print("NAME "+car1.name)
print("SPEED "+car1.speed)
print("DOOR "+car1.door)

car1.updatecolor("UPDATE COLOR "+"PINK")
print(car1.color)

car1.updatespeed("UPDATE SPEED "+"555km/h")
print(car1.speed)

car1.updatedoor("UPDATE DOOR "+"5")
print(car1.door)





print("-------------------------------------------- \n                    car3\n--------------------------------------------")
car3=car("2003","grey","mehran","255km/h","4")
print("MODEL "+car1.model)
print("COLOR "+car1.color)
print("NAME "+car1.name)
print("SPEED "+car1.speed)
print("DOOR "+car1.door)

car1.updatecolor("UPDATE COLOR "+"YELLOW")
print(car1.color)

car1.updatespeed("UPDATE SPEED "+"355km/h")
print(car1.speed)

car1.updatedoor("UPDATE DOOR "+"5")
print(car1.door)


print("-------------------------------------------- \n                    car4\n--------------------------------------------")
car4=car("2004","black","honda","855km/h","4")
print("MODEL "+car1.model)
print("COLOR "+car1.color)
print("NAME "+car1.name)
print("SPEED "+car1.speed)
print("DOOR "+car1.door)

car1.updatecolor("UPDATE COLOR "+"PINK")
print(car1.color)

car1.updatespeed("UPDATE SPEED "+"955km/h")
print(car1.speed)

car1.updatedoor("UPDATE DOOR "+"5")
print(car1.door)


print("-------------------------------------------- \n                    car5\n--------------------------------------------")
car5=car("2005","white","mercedes","1005km/h","4")
print("MODEL "+car1.model)
print("COLOR "+car1.color)
print("NAME "+car1.name)
print("SPEED "+car1.speed)
print("DOOR "+car1.door)

car1.updatecolor("UPDATE COLOR "+"BLUE")
print(car1.color)

car1.updatespeed("UPDATE SPEED "+"1100km/h")
print(car1.speed)

car1.updatedoor("UPDATE DOOR "+"5")
print(car1.door)


# In[ ]:




