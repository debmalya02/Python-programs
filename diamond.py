# General formula for diamond pattern
def pat(n):
    for i in range(1,n+1):
        for j in range(n,i,-1):
            print(end=' ')
        for j in range(1,i+1):
            print(j,end=' ')
        print('')
    for i in range(n,1,-1):
        for j in range(0,n+1-i):
            print(end=' ')
        for j in range(1,i):
            print(j,end=' ')
        print('')