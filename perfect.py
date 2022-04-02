n=100
print('Perfect number from 100 to 1 is: ')
while n>1:
    i=1
    s=0
    while i<n:
        if (n%i==0):
            s+=i
        i+=1
    if(s==n):
        print(n,end=' ')
    n-=1