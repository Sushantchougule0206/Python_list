'''Print two lists in the following order
list1 = [5, 6,7]
list2 = [0, 1]
output:
50,51,60,61,70,71'''

l1=[5,6,7]
l2=[0,1]
l3=[]
x=0

'''for i in range(len(l1)):   
    for j in range(len(l2)):
        x=int(str(l1[i])+str(l2[j]))
        l3.append(x)
print(l3)'''

for i in l1:   
    for j in l2:
        l3.append(int(str(i)+str(j)))

print(x)
print(l3)