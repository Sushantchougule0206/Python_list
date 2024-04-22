'''Remove empty strings from the list of strings
list1 = ["Ashish", "", "Atharva", "Amit", "", "Revati"]
output:
["Ashish", "Atharva", "Amit", "Revati"]'''

list1 = ["Ashish", "", "Atharva", "Amit", "", "Revati"]

#Method 1
'''list1.remove("")
list1.remove("")
print(list1)'''

#Method 2
'''list1.pop(1)
list1.pop(3)
print(list1)'''

#Method 3
list2=[str for str in list1 if str !=""]
print(list2)
