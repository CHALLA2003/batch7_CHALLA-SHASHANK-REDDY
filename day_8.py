# 1.) Write a Python script to generate and print a dictionary that 
# contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 2.)Find the uncommon words from 2 strings

# # s1 = "Hello how are you"
# s2 = "Hello how is"

# 3.)Write a code print the 8th fibanacci number


# ! Eg: 3
# def profile(name, age, place):
#     txt = "My name is {}. I am {} years old. I am from {}."
#     print(txt.format(name, age, place))
# profile("Shashank", 21,"KSRM")

# ! return
#1.) A variable declared inside the function can be accessed outside the function
#    using return
#2.) return does not prrint anything
#3.) we cannot write any code below return statement





#! Eg:4
# ? Function with return statement
# def f1(a, b):
#       z = 8
#f1()
#print(z)  # ---> cannot use outside the function


# def f1(a, b):
#     c = (a*b)
#     return c
# # print(f1(6, 8))
# obj = f1(6, 8)
# obj1 = f1(4, 6)


# def gracemark(object):
#     print(object+4)
# gracemark(obj)
# gracemark(obj1)

# ! problem:1
# def palindrome(n):
#     string = str(n)
#     rev = str(n)[::1]
#     if string==rev:
#         print(n, "Palindrome")
#     else:
#         print("Not palindrome")  
# a = int(input("Enter the value: "))
# palindrome(a)

# ? Based on the declaration of parameters and args
# ? functions are divided into 5 categories


#Positional args
#keyword args
#default args
#variable length args
# keyword variable length args
# Positional args



# * Positional args
# ? The position of parameter have to be same as position as arguments
# def profile(name,phone,mark):
#     txt="My name is{}. My phone number{}. I got{} marks{}."
#     print(txt.format(name,phone,mark))
# profile(9852569420,"Shashank",100) #unexpected

# * Keyword args
# ! Eg:1
# ? To overcome the disadvantage of psition args, we use keyword args
# ? It is a process of initialising the parameter with the args while calling the
# ? Function
# def profile(name, phone, mark):
#     txt="My name is{}. My phone number{}. I got{} marks{}."
#     print(txt.format(name,phone,mark))

# profile(name = "shashank", mark=96, phone=9876543210)



# * todo --> Exception of keyword args function
# def profile(name, phone, mark):
#     txt="My name is{}. My phone number{}. I got{} marks{}."
#     print(txt.format(name,phone,mark))

# profile(name = "shashank", mark=99, phone=9876543210) # Error
# profile(9876543210,name= "shashank", mark=99) # error
#profile("shashank",mark=98,phone=9876543210) 


# * Default args
# The method of assigning the argument to the parameter while declaring the
# Function
# ! Eg:1
# def profile(name, phone, mark):
#     txt="My name is{}. My phone number{}. I got{} marks{}."
#     print(txt.format(name,phone,mark))
    
# profile("Shashank", 9876543210)

# !  Eg:2
# def profile(name, phone, place="Kadapa"):
#      txt="My name is{}. My phone number{}. I got{} marks{}."
#      print(txt.format(name,phone,place))
    
#profile("Shashank", 9876543210, "Guntur")

#Problem Statement – Given a string S(input consisting) of ‘*’ and ‘#’. 
#The length of the string is variable. The task is to find the minimum number of ‘*’ 
#or ‘#’ to make it a valid string. The string is considered valid if the number of ‘*’ 
#and ‘#’ are equal. The ‘*’ and ‘#’ can be at any position in the string.
#Note : The output will be a positive or negative integer based on number of ‘*’ 
#and ‘#’ in the input string.

#(*>#): positive integer
#(#>*): negative integer
#(#=*): 0
# --->Example 1:
#Input 1:

###***   -> Value of S
# Output :

# Eg:2
# def profile(name, phone, place="Kadapa"):
#     if place == "kadapa" or place=="kADAPA" or place=="Kadapa":
#      txt="My name is{}. My phone number{}. I got{} marks{}."
#      print(txt.format(name,phone,place))
#     else:
#         print("You are not eligible to Signup")
# profile("Shashank",9876543210)

# ! Exception
# def profile(name, phone, place="Kadapa"): # error --> because default args should not follow positional param
#     if place == "kadapa" or place=="kADAPA" or place=="Kadapa":
#      txt="My name is{}. My phone number{}. I got{} marks{}."
#      print(txt.format(name,phone,place))
#     else:
#         print("You are not eligible to Signup")
# file("Shashank",9876543210)


# ! Variable length params
# ! Eg:1
# To pass more then 1 arg to a parameter means we use variable length args
# To convert normal parameter to variable length param, add* to their prefix of param

# name = "sid", "name2", "name3"
# def profile(*name):
#     for val in name:
#         print("My name is",val)
# profile("shashank",'rajesh', 'umar')


# ! ----> Object Oriented Programming
# The panadigms of objects oriented progarmming are


# class
# objects
#inheritance
#polymorphism
#abstraction
# encapsulation

#  ! Class is a blue print of an object
# l1 = {1, 2, 3, 4, 5, 6 }

# ? Eg:1
# class c1:
#     name1 = "Shashank" 
#     print(name1)

# ? Eg:2
# class person:
#     name="Shashank"
# The process of creation of an object is called as Instantation()
# c = person() # c as object
# print(c.name)


# ? Eg:3
# create of a method
# When the function is created with a class is called as method

# class person:
#     def display(person): # It is a method
#         print("Hello welcome to classes")
        
# p = person()
# p.display()


# ? Eg:4
# ! method with parameter
# class person:
#     def display(person, name, age):
#         print(name, age)
        
# p = person()
# p.display("Shashank", 21) 

# ! Eg:5
# class person1:
#     fname = "Shashank" # attribute or static variable
#     lname = "C"
    
#     def first_name(self):
#         print(self.fname)
        
#     def full_name(self):
#         print(self.fname+" "+self.lname)
        
# p = person1()
# p.first_name()
# p.full_name()

# ? Eg:6
# constructors --> __init__()
# This is a special method which has the ability to execute itself without
# calling it manually through the process of instantiation

# class profile:
#     def __init__(self):
#         print("hey")
    
    
# p = profile() # execution of constructor through this process









