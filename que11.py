num=int(input('Enter the number: '))

max=0

for i in range(5):
    digit=num%10
    if max<num:
        max=num
print(max)