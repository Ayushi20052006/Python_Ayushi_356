# list1=["Ayushi",5,"seven",6.7]
# print(list1)

# #NO OF ELEMENTS IN LIST ==> len
# print (len(list1))

# #LIST CONNSTRUCTOR
# list2=list(("Seven",6,5,"Ayushi",9,"ABES"))
# print (list2)

# #ACCESSING LIST ELEMENTS
# print (list2[1])
# print (list2[-1])
# print (list2[-3:-1])   #TO PRINT CERTAIN RANGE OF ELEMENTS

# #TO CHECK PRESENCE OF CERTAIN ITEM IN LIST
# if "Ayushi" in list2:
#     print("yesss")
    
    
# if "DEV" in list2:
#     print("yes")
# else:
#     print("nooooo")


# #MODIFICATION OF LIST
# list2[1]="ABHI"
# print(list2)
# list2[0:2]=[7,"AVINASH"]
# print(list2)

# #INSERTING ELEMENTS IN LIST
# list2.insert(0,"AYUSHI")
# print(list2)

# #APPENDING A ELEMENT IN LIST
# list2.append("World")
# print(list2)

# #DELETING AN ELEMENT FROM LIST
# list2.remove(7)
# print(list2)

# #DELETING AN ELEMENT FROM A PARTICULAR INDEX
# list2.pop(3)
# print(list2)

# #TO PRINT VALUES OF A LIST
# #METHOD 1
# for x in list2:
#     print(x)
# print()
# #METHOD 2
# for i in range(len(list1)):
#     print(list1[i])
# print()
# #METHOD 3
# i=0
# while(i<len(list1)):
#     print(list1[i])
#     i=i+1
# print()
# #METHOD 4
# [print(x) for x in list1]


# #TO DELETE THE FULL LIST
# del(list1)

# #TO REMOVE DATA FROM LIST WITHOUT DELETING THE LIST
# list2.clear()
# print(list2)
# del(list2)


#TO COPY AND PRINT ELEMENTS IN CAPITAL AND IN UPPER CASE
list=["apple","mango","cherry","kiwi","Papaya"]
fruits=[x.upper() for x in list]
print(fruits)
fruits=[x.capitalize() for x in list]
print(fruits)

#TO PRINT THE LIST IN REVERSE ORDER
list.reverse()
print(list)

#SORTING OF LIST
list.sort()
print(list)