list1=["Ayushi",5,"seven",6.7]
print(list1)

#NO OF ELEMENTS IN LIST ==> len
print (len(list1))

#LIST CONNSTRUCTOR
list2=list(("Seven",6,5,"Ayushi",9,"ABES"))
print (list2)

#ACCESSING LIST ELEMENTS
print (list2[1])
print (list2[-1])
print (list2[-3:-1])   #TO PRINT CERTAIN RANGE OF ELEMENTS

#TO CHECK PRESENCE OF CERTAIN ITEM IN LIST
if "Ayushi" in list2:
    print("yesss")
    
    
if "DEV" in list2:
    print("yes")
else:
    print("nooooo")


#MODIFICATION OF LIST
list2[1]="ABHI"
print(list2)
list2[0:2]=[7,"AVINASH"]
print(list2)

#INSERTING ELEMENTS IN LIST
list2.insert(0,"AYUSHI")
print(list2)

#APPENDING A ELEMENT IN LIST
list2.append("World")
print(list2)

#DELETING AN ELEMENT FROM LIST
list2.remove(7)
print(list2)

#DELETING AN ELEMENT FROM A PARTICULAR INDEX
list2.pop(3)
print(list2)