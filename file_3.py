#Day3



# ! Eg:3
#  Take values of length and breadth of a
# from user and check if it is square or not
'''
length = int(input("enter length: "))
breadth = int(input("enter breadth: "))
if (length == breadth):
    print("It is a square ")
else:
    print("Not a square")
'''


# ! Eg: 4
# Python program to check whether the
# given integer is a multiple of both 5 and 7

'''
a = int(input("Enter a number: "))
if (a%5==0 & a%7==0):
    print("Yes")
else:
    print("No")
'''  

# ! Eg: 5
# Write a program to accept the cost price of a bike and display the
# road tax to be paid
# according to the following criteria :


#         cost price(in Rs)        Tax
#       > 100000                 15 % + discount 6%
#       < 100000                 5%

'''
price = int(input("enter the price: "))
total = 0
if price>=100000:
    discount = 100000*(6/100)
    value = price-discount
    amount=value*(15/100)
    total=value + amount
else:
    tax = price*(5/100)
    total = price + tax
print("The Onroad cost of bike is : ", total)
'''


# ! Eg: 6
# Accept the age of 4 people and display the oldest one
'''

a=int(input("enter first person age: "))
b=int(input("enter second person age: "))
c=int(input("enter third person age: "))
d=int(input("enter fourth person age: "))
if(a>b and a>c and a>d):
    print("a is oldest")
elif(b>a and b>c and b>d):
    print("b is oldest")
elif(c>a and c>b and c>d):
    print("c is oldest")
elif(d>a and d>b and d>c):
    print("d is oldest ")

    
'''





# ! -----> Short hand if else
# Eg:1
'''    
a = 9
b = 60
if a>b:
     print("a")
else:
     print("b")

     
'''

#Rules
#1.)statement inside the if condition have to be present at first
#2.) elif cannot be used in short hand if else
#3.) Always it have to end with else

# print("A") if a>b else print("B")

#  ---> Eg:2

#A school has following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A
# Ask user to enter marks and print the corresponding grade.

'''
marks=int(input("enter the Marks:  "))
if (marks>=80):
    print("A")
elif(marks>=60 and marks<80):
    print("B")
elif(marks>=50 and marks<60):
    print("C")
elif(marks>=45 and marks<50):
    print("D")
elif(marks>=25 and marks<45):
    print("E")
elif(marks<=25):
    print("F")
'''




# ! Code to check the given char is vowel or constant
#char = input("Enter the char: ")
# if char=="a" or char =='e' or char=='i' or char == 'o' or char =='u':
#print("is a vowel")
# else:
#print("it is a consonant")

# ? or
#str1 = "aeiouAEIOU"
#if char in str1:
    #print("vowel")
#else:
    #print("consonent")


#! shortand if else
'''
char = input("Enter the char: ")
str1 = "aeiouAEIOU"
print("vowels") if char in str1 else print("consonent")
'''


# ---> elif ladder using short hand if else
#Eg:1
# ? Find greatest among 3 variables using short hand if else
a = 8
b = 5
c = 9

#print("A is greater") if a>b and a>c else print("B is greater")
#if b>a and b>c else print("C is greater")



# ! -----------> looping

# looping can be implemented using
# for loop
# while loop


# ----> for loop
#?for loop is used for iterations, if we know the numbers of times the loop have to run
#?It is used to iterate the iterables eg(string, list, tuple, etc...)


# todo ---> Syntax for loop

# for syntax in c
# for(i=0;i<10;i++){
#   printf("hello");
# }


# ! for syntax in python
# for userdefined_variable in range(start, end, step): default step value is 1
# statement
# statement 
# statement


# ? Eg: 1
# To print the value from 1 to 10 using for loop



#for i in range (0, 10) : #(n, n-1)
    #print(i)
    #print("hello")



# Eg:2
#for val in range(208, 252):
    #print(val)
    
    
#for val in range(1, 1000, 5):
    #print(val)


# ? Eg : 3
# to decrement the value

#for val in range(10, 0, -1):
    #print (val)

#for val in range(10, 0, -2):
    #print (val)

#for val in range(10, 0, 1):
    #print (val) # no output



# ? Eg:4
# ! Print the output of 7th multiplication table from 21 to 43
#for val in range(21, 43, 7):
    #print(val)

 #for val in range(1, 10+1, ):
   #print('7','x',val,'=',val*7)--------> Method 1



   # ans = "7X{} ={}"    -----> method 2
   #print(ans.format(val, val*7))


# ----> method 3:

#for val in range(1, 10+1, ):
    #print(f"7 X {val}={val*7}")


'''
# ? Eg: 5
# break statement


for val in range(1, 10):
    if val == 6:
        break
    print(val)


# ? Eg: 6

for val in range(1, 10):
    print(val)
    if val == 6:
        break



# Eg: 7


for val in range(1, 10):
    if val == 6:
        print(val)
        break

'''



# ! continue
# Eg:1
#for val in range (1,10):
    #if val ==6:
        #continue
    #print(val)

'''


for val in range(1, 30):
    if val == 6 or val ==8 or val ==21:
        continue
    print(val)
'''

# ! practise problems
# ? print the even number between 20 to 40


#for i in range(20, 41):
    #if i%2==0:
       # print(i)




#!------> While loop
# while is used when we do not know the number of times the loop have to run
# ? to iterate the not iterable elements while loop is used


# todo syntax


# initialization
#while condition:
# statement
# increment or Decrement


#Eg:1
# to iterate number from 1 to 10


#i = 0
#while i<11:
   # print(i)
   # i=i+1 # OR I+=1


# For loop practisee
# Write a program to display sum of odd numbers and even
# Numbers that fall between
# 12 and 37 (including both numbers)

for i range of (12, 37)



# -----> Assessment
#1.) cats and mouse: Hackerrank
#2.) Print the factorial of 8 using for loop
#3.) Write a program to display sum of odd numbers and even numbers that fall between 12 and 37 (including both numbers)
# 4.) Write code to print the sum of number using while loop
# n1 = 123 --> 1+2+3 = 6
# 5.) Prine th reverse of given number --> n1= 234 o/p --> 432
    










        
























































    























   
 










































































































































