#s = 2+4+6+......N
n=int(input('Enter the last number: '))
i = 2
s=0
print('The sum of: ',end=' ')
while i<=n:
    print(i,end=' ')
    s=s+i
    i+=2
print('is ',s)
print('\n')

#s = 1 + 2² + 3³ + .......N
n=int(input('Enter the last number: '))
i = 1
s=0
print('The sum of: ',end=' ')
while i<=n:
    s=s+i**i
    i+=1
print('is ',s)
print('\n')

#s = 1 + (1*2) + (1*2*3) + ........N
n=int(input('Enter the last number: '))
i = 1
s=0
f=1
print('The sum of: ',end=' ')
while i<=n:
    s=s+(f*i)
    f=f*i
    i+=1
print('is ',s)
print('\n')