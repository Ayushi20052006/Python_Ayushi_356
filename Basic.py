# i=1;
# print(type(i));
# print(id(i));

#multiple variable
# a,b,c=1,2,3;
# print(a,b,c);

# print(id(a));
# print(id(b));
# print(id(c));

# a=b=c;
# print(id(a));
# print(id(b));
# print(id(c)); #(same as c)



#variable naming-
# 1-camel style:- myVariable
# 2-snake style:- my_variable
# 3-pascal style:- MyVariable

#datatypes
# var1=1  #integer
# var2=True   #boolean
# var3=10.567   #float
# var4=10+6j     #complex
# print(id(var1))
# print(type(var1))
# print(id(var2))
# print(type(var2))
# print(id(var3))
# print(type(var3))
# print(id(var4))
# print(type(var4))

#STRINGS(Multiline and single line string)(Strings are also trated as array ie. they allso have indexing)
# multiline---- 
# a = """
# hello 
# how
# are
# you
# """
#Singleline string
#a="Hello how are you"

#COUNTING NO OF ELEMENTS IN STRING --> len()

# text="Hello how are you. Great to see you "
# if "are" in text:
#     print("Yes")
# else:
#     print ("No")
    
    
#STRING SLICING
# a="Hello my name is Ayushi"
# print(a[2:15])
# print(a[0:5])

# a=" Ayushi "
# print(a.strip()) #removes spaces

# #replace
# print(a.replace("Hello","Ayushi"))

# a="Hello, world"
# print(a.split(","))  #['Hello', ' world']
# a="Hello world, Ayushi here"
# print(a.split(","))  #['Hello world', ' Ayushi here']
#here "," works as a seperator

#string concatenation
# a="hello"
# b="world"
# c=a+" "+b
# print(c)   #hello world

# #format-strings (F-string)
# age=19
# t=f"my name is Ayushi,I am {age}"
# print(t)

# price=12.5567
# txt=f"the price is {price:.2f} dollar"
# print(txt)

# output
# my name is Ayushi,I am 19
# the price is 12.56 dollar

#Escape character-to insert characters that are illegal in a string(backlash-\)
#for eg- using double quote inside a string surrounded by double quote
# txt="we are the so-called \"vikings\" from the north."
# print(txt)    #we are the so-called "vikings" from the north.

#Boolean-(True or False)
# print(10>9)           # True
# print(10<9)           # False
# print(bool("hello"))  # True
# print(bool(10))       # True
# print(bool(0))        # False

# #function returning boolean
# def fun():
#     return True

# if fun():
#     print("yes")
# else:
#     print('no')

#SEQUENCE DATA TYPES- LIST , TUPLE , RANGE
 
#list
l=["Ayushi",19,"21-may-2006","BTech"]
tiny_l=["CSE",14]
print(type(l))
print(l)
print(l[0])
print(l[1:3])
print(l[2:])
print(tiny_l *2)
print(l+tiny_l)
#output
# <class 'list'>
# ["Ayushi",19,"21-may-2006","BTech"]
# 
# [19, '21-may-2006']
# ['21-may-2006', 'BTech']
# ['CSE', 14, 'CSE', 14]
# ['Ayushi', 19, '16-may-2006', 'BTech', 'CSE', 14]

#tuple
tup=("abcd",789,4.56,"john",20+8j)
tiny_tup=(123,"hello")
print(type(tup))
print(tup)
print(tup[0])
print(tup[1:3])
print(tup[2:])
print(tiny_tup *2)
print(tup+tiny_tup)
#output
# <class 'tuple'>
# ('abcd', 789, 4.56, 'john', (20+8j))
# abcd
# (789, 4.56)
# (4.56, 'john', (20+8j))
# (123, 'hello', 123, 'hello')
# ('abcd', 789, 4.56, 'john', (20+8j), 123, 'hello')

#range(start,stop,step)
for i in range(5):
    print(i)   #01234

for i in range(1,10,2):
    print(i)   #13579

#INPUT
# n=int(input(""))
# print(n)  
# print(type(n))

a=5
b=10
# if a>b:
#     print(a," is greater than ", b)
# elif a==b:
#     print("both are equal")
# else :
#     print(b," is greater than ",a)
    
#SHORTHAND
print(f"{a} is greater than {b}") if a>b else print(f"{b} is greater than {a}")
print(f"{a} is greater than {b}" if a > b else "=" if a == b else f"{b} is greater than {a}")
