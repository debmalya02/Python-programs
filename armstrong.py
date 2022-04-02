n = int(input('Enter the number: '))
i = n
f=n
s = 0
while i>0:
    n = i%10
    s += n**3
    i = i//10
if s==f:
    print('The number is Armstrong number')
else:
    print('The number is not an Armstrong number')

#Amstron number from 100 to 999
n=100
while n<=999:
    i=n
    f=n
    s=0
    while i>0:
        f = i%10
        s += f**3
        i = i//10
    if s==n:
        print(n,end=' ')
    n+=1