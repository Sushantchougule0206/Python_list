'''Given a two Python list. Iterate both lists simultaneously such that list1 should display item in original order and
list2 in reverse order.
It should work for any two lists.
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
output:
10 400
20 300
30 200
40 100'''
l1=[10,20,30,40]
l2=[100,200,300,400]
l2=l2[::-1]
for i in range(len(l1)):
    for j in range(len(l2)):
        print(l1[i],l2[j])
        break
    j+=1