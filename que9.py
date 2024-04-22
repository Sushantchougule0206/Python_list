'''Given a Python list, find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of a value
list1 = [5, 10, 15, 20, 25, 50, 20]'''

'''l1=[5, 10, 15, 20, 25, 50, 20]
idx=l1.index(20)
l1[idx]=200
print(l1)'''

l1=[5, 10, 15, 20, 25, 50, 20]

for i in range(len(l1)):
    if l1[i]==20:
        l1[i]=200
        break
print(l1)
