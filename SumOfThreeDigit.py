n=int(input('Enter any digit number: '))
i=n
s=0
print('The sum of',end=' ')
while i>0:
    n = i%10
    print(n,'+ ',end='')
    s = s+n
    i = i//10
print('= ',s)