#DICTIONARY=> Contains key-value pair
# del d[key] => To delete a key value pair from dictonary


d={
  "brand": "Ford",
  "model": "Mustang",
  "mode": "petrol",
  "year": 1964
}
#ACCESSING ITEMS OF DICTIONARY
print (d)   #to print full dictinary
for x in d:
    print (x)    #to print keys
    print (d[x])    #to print values
    
print (d.keys())   #To print keys
print (d.values())   #To print values

#DELETING ITEMS FROM DICTIONARY
d.popitem()   #TO DELETE LAST ITEM
print(d)
d.pop("brand")    #TO DELETE PARTICULAR KEY VALUE PAIR
print(d)
del d["mode"]     #TO DELETE PARTICULAR KEY VALUE PAIR