# ----> Assesment
# 1.) dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# Merge two python dictionary
# o/p --> {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# d1={'Ten':10,'Twenty':20,'Thirty':30}
# d2={'Thirty':30,'fourty':40,'fifty':50}
# d1.update(d2)
# print(d1)



# 2.)Python Program to determine if 
# the given Sets Are Disjoint 
# or Not without Using Inbuilt-in Functions

# set1 = {'Python', 'Java', 'Data Science'}
# set2 = {'ML', 'AI', 'R Language', 'Python'}
# set3 = {'Data Analytics', 'Robotics', 'Deep Learning'}


# set1 = {'Python', 'Java', 'Data Science'}
# set2 = {'ML', 'AI', 'R Language', 'Python'}
# set3 = {'Data Analytics', 'Robotics', 'Deep Learning'}
# c = 0
# flag=0
# for val in range(3):
#     c=c+1
#     if c==1:
#         for val in set1:
#             if val in set2 or val in set3:
#                 flag=1
#                 break

#     if c==2:
#         for val in set2:
#             if val in set1 or val in set3:
#                 flag=1
#                 break

#     if c==3:
#         for val in set3:
#             if val in set2 or val in set1:
#                 flag=1
#                 break

# if flag == 0:
#     print("disjoint")
# else:
#     print("joint")

# 3.)list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]

# O/P --> ['My', 'name', 'is', 'Kelly']

# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]

# result = [list1[i] + list2[i]
# for i in range(len(list1))]

# print(result)

# or

#l3 = []
# for val in range(len(list1)):
#     ans = list1[val]+list2[val]
#     l3.append(ans)
# print(l3)

# or 

# i = 0
# while i < len(list1):
#     l3.append(list1[i] + list2[i])
#     i += 1
# print(l3)

# Hacker Rank ---l> Caesar Ciper

# ! Functions
#? DEF
# Function is a block of code which is used to perform a specific functionally
# Function can be created using def keywords

# Function has 3 parts
# Function declaration
# Function definition
# Function call  

# def greet():
#     print("Greetings User!!")
    
# greet()
# greet()
# greet()
# greet()
# greet()
# greet() # Function calling


# Eg:1

# def adding():
#     a = int(input())
#     b = int(input())
#     c = int(input())
#     d = a+b+c
#     print(d)
# adding()
# adding()

# Eg:2
# ? Function with parameter
# def greeting(name):
#     print("Welcome", name)
    
    
# for val in range(3):
#     username = input("Enter the name: ")
#     greeting(username)  #Username is argument


# ! Eg:3
# def profile(name, age, place):'
#     print(name, age, place)
# profile("SHASHANK","21", "KADAPA")

#1.) Write a Python script to generate and print a dictionary that 
# contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 2.)Find the uncommon words from 2 strings

# # s1 = "Hello how are you"
# s2 = "Hello how is"

# 3.)Wrire a code print the 8th fibanacci number









