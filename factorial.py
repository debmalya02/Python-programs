n=int(input('enter the number: '))
f=1
print('factorial of the number is: ',n,'! =',end=' ')
while n>0:
    print(n,'* ',end='')
    f = f*n
    n -= 1
print(' = ',f)