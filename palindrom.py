n=int(input('Enter the number: '))
i=n
f=n
r=0
while i>0:
    n = i%10
    r = (r*10)+n
    i = i//10
if (r==f):
    print('This is a palindrom number')
else:
    print('This is not a palindrom number')