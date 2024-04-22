'''Given a Python list of numbers. Turn every item of a list into its square root
aList = [1, 4, 9, 16, 25, 36, 49] 
output:
[1, 2, 3, 4, 5, 6, 7]'''
l1=[1,4,9,16,25,36,49]
l2=[]
a=1
for ele in l1:
    b=int(ele/a)
    l2.append(b)
    a+=1
print(l2)
