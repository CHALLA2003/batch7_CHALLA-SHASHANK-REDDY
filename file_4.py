# Day 4


#----> While loop
#----> Break using while loop

#Eg: 1
#1.)iterate from  20 to 30 and break the loop in 27
'''
i = 20
while i<31:
    if i ==27:
        break
    print(i)
    i+=1
'''

'''
# ----> Eg:2

i = 20
while i<=30:
    print(i)
    i+=1
    if i  == 27:
        break



# ----> Eg:3

i = 20
while i<31:
    print(i)
    if i  == 27:
        break
    i+=1


# ----> Eg:4

i = 20
while i<31:
    if i== 27:
        print(i)
        break
    i+=1
'''


# ----> Continue
# -----> Eg:1
'''
i = 20
while i<31:
     if i ==27:
          continue
     print(i)
     i=i+1
'''



# -----> Eg:2
'''
i = 20
while i<31:
     i=i+1
     if i ==27:
          continue
     print(i)
'''


# -------------> Eg: 5
#While to iterate from 12 to 22
# Find the sum of all integers

'''
i = 12
sum=0
while i<23:
    sum=sum+i
    i+=1
print(sum)
'''

# ! ----> Eg:6
# Find the average of value from 20 to 25
'''
i = 20
avg = 0
sum = 0
while i<26:
    sum=sum+i
    i+=1
    avg=(sum/6)
print("avg is : ",avg)
 '''   
# Find the average of value from 20 to 30
'''
i= 20
sum = 0
count = 0
while i<=30:
    sum = sum+i
    count+=1
    i+=1
print(sum/count)
'''

# ----> Nested for loop
# Eg:1
'''
for i in range(1, 3+1):
    for j in range(1, 4+1):
        print(i, j)
'''

# ------> Eg:2

# * * * *
# * * * *
# * * * * 
# * * * *
'''
rows = int(input("enter the rows: "))
cols = int(input("enter the cols: ")) 

for row in range(rows):
    for col in range(cols):
        print("*", end = " ")
    print()
 
    



for row in range(5):
    for col in range(5):
        print(row, end = " ")
    print()

    
'''
'''
sum = 0
for row in range(5):
    for col in range(5):
        sum = sum+1
        print(sum, end = " ")
    print()
 
 '''  

# ! to print stars in right angled triangle
'''
*
* *
* * * 
* * * * 
* * * * *
* * * * *



for row in range(0, 6):
    for col in range(0, row+1):
        print("*", end = " ")
    print()

 




* * * * * *
* * * * *
* * * *
* * *
* *
*



for row in range(0, 6):             
    for col in range(row, 6):
        print("*", end = " ")
    print()

    
'''
# Eg:
'''
* * * * *
*       *
*       *
*       *
* * * * *      

for row in range(5):             
    for col in range(5):
        if col == 0 or col ==5-1 or row == 0 or row == 5-1:
            print("*", end = " ")
        else:
            
            print(" ", end = " ")
    print()

'''
'''
#          *
#        * * *
#       * * * *
#      * * * * * 
    
for row in range(0, 5):             
    for col in range(0, 6):
        if ((row==0 and col==3) or (row==1 and (col>=2 and col<=4)or (row==2 and (col>=1 and col<=5)))):
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()
'''

#*
#* *
#*   *
#*     *
#*       *
#* * * * * *
'''
for row in range(0, 6):             
    for col in range(0, 6):
        if(col==0 or (row==0 and col==0) or (row==1 and col==1))or (row==2 and col==2) or (row==3 and col==3) or (row==4 and col==4) or (row==5):
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()
'''
# -----> List
#  ! ----------. Data Types
#Primary

# Number ---> int, float complex
# String
#Boolean
#None

#Collection
#List
#Tuple
#Set
#Dictionary

# ? ---> List

# 1.) if the collection of elements are surrounded by Square brackets, it is considered to be list.
# ! ---> Eg:
# l1 = [4, 7, 9, 9.89, "hello", 7+9j, [8, 9, 0]]


# Characteristics of list
# 1.) List have to be surrounded []
# 2.) It is mutable (the elements in the list are changable)
# 3.) Every elements inside list is indexed
# 4.) The elements inside list will be ordered format
# 5.) It can hold duplicate values
# 6.) Its heterogenous

# To access the elements in list
#lst1 = [1, 4, 1, 7, 89.7, 75, "p", "i"]
#print(lst1)


# ----> Indexing
# In the collection datatypes like list, tuple, string, the elements will be alloted with predefines unique value called index value

# We have 2 types of indexing
# Positive Indexing ---> starts with 0 from left hand side
# Negative Indexing ---> starts with -1 from right hand side



# Positive Indexing
#print(lst1[0])
#print(lst1[4])
#print(lst1[20]) ---> Error



# ? ---> Negative Indexing
'''
lst1 = [1, 4, 1, 7, 89.7, 75, "p", "i"]
print(lst1[-1])
print(lst1[-5])
'''
# ----> Slicing
#lst1 = [1, 4, 1, 7, 89.7, 75, "p", "i"]
#lst1[start_index:end_index:step]
#print(lst1[0:4])
#print(lst1[6:8])
#print(lst1[3:6])
#print(lst1[:5])
#print(lst1[3:])
#print(lst1[:])



#print(lst1[0:7:1])   # lst1[0:7]  ---> both are same
#print(lst1[0:7:2])



# trail = int(input())
lst1 = [1, 4, 1, 7, 89.7, 75, "p", "i"]
#print(lst1[-4:-1])
#print(lst1[-1:-4])   ----> []
#print(lst1[-7:1])
#print(lst1[-7:1:2])





#! ---> To insert ot add element inside list
# append()-> used to add elelement at last position of list
#l1 = [9, 8, 0, 6]
#l1.append("car")
#print(l1)



'''
n = int(input("enter the number of inputs: "))
for i in range(0, n):
    a, b = list(map(int, input().split()))
    print(a,b)
'''






































































































    
