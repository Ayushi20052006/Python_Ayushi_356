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
    
a="Hello my name is Ayushi"
print(a[2:15])
print(a[0:5])