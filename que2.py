'''take a list 'l1' of even nos between 150 to 250. Print its length.
Then create another list 'l2' using 'l1', containing only nos divisible by 4 from 'l1'.'''
l1=[152,176,196,204,208,212]
print(len(l1))
l2=[ele for ele in l1 if ele%4==0]
print(l2)