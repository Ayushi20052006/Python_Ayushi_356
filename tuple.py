#TUPLE => used to store multiple items in a single variable
#      => ordered and unchangable (immutable)
#      => To change the tuple convert it into list 
#      => TUPLE CONSTRUCTOR =>  tuple()

#INITIALIZATION OF TUPLE
mytuple=("Ayushi","Avi", "Aman","Ravi","Akash","Shivi","Yuvi")
#ACCESSING ELEMENTS OF TUPLE
print(mytuple[1])
print(mytuple[-1])
if "Ayushi" in mytuple:
    print ("Yes Ayushi is present")
else:
    print (f"No Ayushi is not present")
#METHOD 1 to add elements in tuple
L=list(mytuple)
L[4]="Ayush"
L.append("Rakesh")
mytuple=tuple(L)
print (mytuple)
#METHOD 2 to add element in tuple
y=("Abhi",)
mytuple+=y
print (mytuple)



#PACKING AND UNPACKING IN TUPLE
tup=("AYUSHI","AVI")
a,b=tup
print(a)
print(b)
