# day 1 python
# print("hello world")
# print("ahom is my name, hello world")
# print(23)

# # print(24)
# print(22+35)


# Variables
# #a variable is  name giben to a memory location in a program

# name= "ahom"
# age= 23  
# price= 14.99 #here ahom 23 and 14.99 is value





# # print("my name is :",name )

# print("my name age is:", age)
# print("my price:",price )

# Rules for identifiers 
# identiers can be combination of uppercase and lowercase latter, digits or an underscore(_)
# an identifier can not start with digit. so whie variable1 is valid, 1 variable is not valid
# we can't use spacial sysmbols like !,#,@, %, $

# print("my name is ahom das")
# print("age is 18 years old")
# print()

# String sentence words paragraph
# age is integer value
# decimal value is float



# Data types
# Integers  +value, -value , 0
# Strings  ahom das, nabbendu (we can use '',"",''' ''')
# Float 3.5, 5.3 9.10 
# Boolean True and False 
# None no value store

# age = 23
# old = False
# a = None

# print(type(old))
# print(type(a))

# keywords
# keywords are reserved words in python
# and as assert break class continue 
# def del elif else except finally false for from global 
# if import in is lamda
# nonlocal None not or pass raise return True try with while yield



# Case sensitive language
# a and A both variable are different 


# print Sum 

# a=3
# b=3
# print(3+3)


# a=3
# b=5
# sum= a+b
# print(sum)

# a= 1000
# b= -400
# print(a, b)

# Types of Tokens

# Punctuators
# punctuators are symbols to organize sentence in programming
# (),{},@, [], # etc.


# -= , +=, /= 

# Types of Operators
# An operator is a symbol that performs a certain operation between operands
# Arithmetic Operators(+, -, *, /, %, **)
# Relational Opeartors/Comparison (==, !=, >, <, >=, >=)
# #Assignment Operators (=, +=, -=, /=, *=, **=)
# #Logical Opertors (not, and, or )

# a= 5
# b= 2
# # print(a*b)

# a=5
# b=3
# print(a/b)



# a= 5
# b= 3

# print(round(a/b))

 
# print(a % b)    #remainder value 1 

# a=5
# b=3
# print(a%b) #remainder value 


# print(a%b)

# relational operator 
# != not equaltu , == for is this equal?,
# a=50
# b=20
# print(a==b)
# print(a!=b) 

# a=50
# b=20
# print(a>=b)
# print(a<=b)
# print(a!=b)
# print(a==b)
# print(a<b)
# print(a>b)


# assignment operators

# num=10
# num+= 10
# print(num)
# num=10
# num-=1
# print(num)

# num=10
# num/=10
# print(num)

# num=19
# num*=2
# print(num)


# num=10
# num2= 4
# num**=2
# print("num:", num)

# Logical opearators
# print(not False)
# print(not True)

# a=True 
# b=False 


# # print(not(a<b))

# print("and operator:", a and b )


# and operator always both value should be true

# or operator always if both value should false 


# a=50
# b=20

# val1= True 
# val2=False
# print(not False)
# print(not True)

# print(not (a>b))
# print("and operator:", )


#  print( val1 or val2 )
# val1 = True
# val2= False 

# print(val1 and val2)



# #Type Conversion
# automatically convert 
# a, b= 1,2.0
# sum= a+b
# print(sum)

# a="2"
# b=4.25
# sum=a+b


# print(sum)

# Type casting 
# we have do it manually programmer

# a, b= 1, "2"
# print(type(a))

# a= float("2")
# b= 3.34

# print(a+b)

# a=3.14
# a=str(a)
# print(a)
# print(type(a))

# input in python 

# input("enter your name ")


# name= input("enter your name ")
# print("welcome:" , name )

# name = input("what's your name ")
# age= input("what's your age")
# price= input("what's your current salary")
# print("welcome",name)
# print("your age is :", age)
# # print("your price is:", price)
# val= input("enter some value:")
# print(type(val))



# val = int(input("enter some value:"))
# print(type(val))




# name= input("enter your name: ")
# age= input("enter your age:")
# marks= input("enter your marks:")



# let's practice
# WRITE A PROGRAM TO INPUT 2 NUMBERS AND PRINT THEIR SUM.
# a=int(input("write first number:"))
# b=int(input("write second number"))
# print(a+b)

# #wap to input side of square and print its area

# a=float(input("square:"))

# print(a*a)



# wap to input 2 floating pint numbers and print their average

# firstnum=float(input("enter your first number:"))
# secondnum=float(input("enter your second number:"))
# ave=firstnum+secondnum
# print(ave/2)


# wap to innput 2 int numbers a and  print True if a is greater than or equal to b if not print false
# a=int(input("enter first:"))
# b=int(input("enter second"))
# print(a>=b)


# Expression Execution

# String and Numeric values can operate together with *

# A, B= 2, 3

# Txt="@"
# # print(2*Txt*3)


# a, b = "2", 3
# print((a+Txt)*3)   #concatenation string and string 

# Numeric values can operate with all arithmetic operators
# a, b= 2, 3 
# c= 4
# print(a+b)



# Arithmetic expression with Integer and float will result in float
# A, B= 10, 5.0
# c= A*B
# print(c)

# Result of divsion operator with two integers will be float
# A, B= 6, 3
# c= A/B
# print(A/ B)

# integer division with float and int will give int displayed as float 
# a, b= 1.5, 3
# c= a//b
# print(c, a/b)


#Floor gives closest integer, which is lesser than or equal to the float value 


# a, b= 12, -5
# c=a//b
# print(c)



# #Write a program to inut 2 numbers and print their sum
# a=int(input("first number:"))
# b=int(input("second number:"))
# print(a+b)


