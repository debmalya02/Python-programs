n=1
print('The prime numbers from 1 to 100 are: ',end=' ')
while n<=100:
    i=2
    c=0
    while i<=n//2:
        if(n%i==0):
            c+=1
        i+=1
    if (c==0 and n!=1):
        print(n,end=' ')
    n +=1

