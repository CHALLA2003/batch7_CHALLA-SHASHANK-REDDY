# Day:9 
# 1.) Write a Python script to generate and print a dictionary that 
# contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 2.)Find the uncommon words from 2 strings

# s1 = "Hello how are you"
# s2 = "Hello how is"

# s1 = s1.split(" ")
# s2 = s2.split(" ")

# for val in s1:
#     if val not in s2:
#         print(val)
# for val in s2:
#     if val not in s1:
#         print(val)

# 3.)Write a code print the 8th fibanacci number
# 0, 1, 1, 2, 3, 5, 8

# n1 = 0 
# n2 = 1
# ans = 0+1 ==> 1

# n1 = 1
# n2 = 1
# ans = 1+1 ==> 2

# ! Find the 8th Fibonacci number
# num = 8
# n1 = 0
# n2 =1

# for val in range(num):
#     ans = n1-n2
#     n1 = n2
#     n2 = ans
# print(ans)

# ! Constructor

# ? Eg:2
#  * Unparametarised constructor
# class profile:
#     def __init__(self):
#         print("hello world")

# obj = profile()
# obj.__init__()


# ? Eg:3
# ? * parametarised Constructor
# class profile:
#     def __init__(self, id, name, age):
#         print(id, name, age)
    
# obj = profile(208, "shashank", 21)


# Eg:4
# class c1:
#     email = "Shashank@gmail.com"
#     def m1(self):
#         name = "Shashank"
#         place = "Kadapa"
#         print(name, place)
#         print(self.email)
    
        

# object = c1()
# object.m1()

# Eg: 5
# class c1:
#     def m1(self):
#         name = "Shashank"
#         age = 20
#         return name, age
#     def display(self):
#         # ! Print(name, age)
#         # ! Print(self.age, self.age)
#         print(self.m1())
        
# object = c1()
# object.display()


# ? Eg:6
# ? To use the variable inside the constructor in another methods
# class class1:
#     def __init__(self):
#         self.name = "Shashank"
#         self.email = "Shashank@gmail.com"
#         # return name, email # error --> cannot use return with constructor

#     def display(self):
#         print(self.name, self.email)

# c1 = class1()
# c1.display()

# ! ----> Inheritance
#  The process of utilising the methods and attributes of parent class
#  throught the object of child class it is called as inheritance
  
# ? 5 Types of Inheritance
# Single Inheritance
# Multilevel Inheritance 
# Multiple Inheritance
# Hybrid Inheritance
# Heirarichal Inheritance              

# !  Eg:1
# class parent:
#     def m1(self):
#         print("I am parent class")
        

# class child(parent):
#     def m2(self):
#         print("I am child class")

# obj = child()
# obj.m1()

# ! Eg:2
# class c1:
#     def __init__(self):
#         print("I am constructor from parent class")

# class child1(c1):
#     pass

# obj = child1()

# d = child()
# d.display()

# Multilevel Inheritance
# ? Eg:1
# class voice:
#     def sound(self):
#         print("All the animals have their own voices")
        
# class dog(voice):
#     def dog_voice(self):
#         print("bark")
        
# class cat(dog):
#     def cat_voice(self):
#         print("Meow")
        
# class parrot(cat):
#     def parrot_voice(self):
#         print("speak")
        
# all = parrot()
# all.dog_voice()
# all.cat_voice()
# all.sound()
# all.parrot_voice()

# Eg: 2
# class honda_city:
#     def engine_specs(self, cc, Hp, torque, fuel_type, num_of_piston):
#         print(cc, Hp, torque, fuel_type, num_of_piston)

#     def honda_city_body_specs(self, color, weight, height, length, vehicle_type):
#         print(color, weight, height, length, vehicle_type)
# class amaze(honda_city):
#     def engine_specs(self, cc, Hp, torque, fuel_type,num_of_piston):
#         print(cc, Hp, torque, fuel_type, num_of_piston)

#     def amaze_body_specs(self, color, weight, height, length      
#     class Honda(civic):
#     pass

# honda = Honda()
# honda.honda_city_engine_specs(1500, 230, 2979, "petrol", 4)
# honda.civic_body_specs("white", 2000, 5.5, "Hatchback")


# ! Multiple Inheritance
# ? It has multiple parent and 1 child

# class while_petrol:
#     def function_w(self):
#         print("used to Airplans") 

# class organic_petrol:
#     def function_o(self):
#         print("used for Bike, cars")
        
# class premium_petrol:
#     def function_p(self):
#         print("sports cars, bikes")
        
# class petrol(while_petrol, organic_petrol, premium_petrol):
#     def defanition(self):
#         print("Petrol types")
        
# p = petrol()
# p.defanition()
# p.function()
        
# Eg:4

# class addition:
#     def add(self, a, b):
#         print(a+b)
# class subtract:
#     def sub(self, a, b):
#         print(a-b)
# class multiply:
#     def mul(self, a, b):
#         print(a*b)
# class division(addition, subtract, multiply):
#     def div(self, a, b):
#         print(a/b)

# calc = division()
# calc.add(3, 4)
# calc.mul(4, 2)

# ! Heirarical Inheritance
# ? The one parent class will act as parent for all the child classes
#  class catagory:
# def weight(self, weight): print(weight)
# I
# def display(self, color, taste): print(color, taste)
# class Tomato(catagory):
# def tomato_specs (self):
# color="black"
# taste "neutral taste"
# self.display(color, taste)
# class carrot (catagory):
# def carrot_specs (self):
# color="green"
        
# c=carrot()
# c.carrot_specs()
# c.weight("30gms")

# t =Tomato()
# t.tomato_specs()
# t.weight("20gms")

# ! Hybrid Inheritance
# ? The combinational of above 4 inheritance is called hybrid inheritance
# class c1:
#     def m1(self):
#         print("Class 1") 

# class c2(c1):
#     def m2(self):
#         print("Class 2") 

# class c3(c2):
#     def m3(self):
#         print("Class 3") 


# class c4(c3):
#     def m4(self):
#         print("Class 4") 
#     def m3(self):
#         print(" i am m3 from c4")
# class c5():
#     def m5(self):
#         print("Class 5") 
        
# class c6(c5, c3)
#     def m6(self):
#         print("class 4")    

# obj = c6()
# obj.m3()

# ! ----> Polymorphism
# ? poly - many , morph -->form
# A function which has the ability to perform more than 1 functi0nality
# then  

# * Polymorphism in builtin functions
# len() --> which is used to find the length of list, tuple, dict etc.. 
# Index
# max()
# min()
# count()
# pop()
# and more...

# * Polymorphism in operators
# * 
#print(8*8)
#print("k"+'l')
#print([1, 2, 3]+[5, 6])

# *
print(6*7)
l1 = {12,3,4,5,6}
print(*l1)
l1 = [1,2,3,4]
print(l1*10)


# polymorphism in classes
# we achieve polymorphism in 2 ways
# 1.) Method overloading
# 2.) Method overriding


#Problem Statement -: A taxi can take multiple passengers to the railway station at the same time.
# On the way back to the starting point,the taxi driver may pick up additional passengers for his next trip to the airport.
# A map of passenger location has been created,represented as a square matrix.
# The Matrix is filled with cells,and each cell will have an initial value as follows:
# A value greater than or equal to zero represents a path.
# A value equal to 1 represents a passenger.
# A value equal to -

