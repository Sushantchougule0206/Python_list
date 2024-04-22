'''Given a Python list, remove all occurrence of 20 from the list
list1 = [5, 20, 15, 20, 25, 50, 20]'''

l1 = [5, 20, 15, 20, 25, 50, 20]

'''l2=[]
for i in l1:
    if i != 20:
        l2.append(i)
l1=l2
print(l1)'''

l1=[ele for ele in l1 if ele!=20]
print(l1)
