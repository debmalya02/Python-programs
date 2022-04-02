#problem no: 1
for i in range(1,5):
    for j in range (1,5):
        print (j,end='')
    print ("")
print('\n')

#problem no: 2
for i in range(1,5):
    for j in range(1,i+1):
        print(j,end='')
    print('')
print('\n')

#problem no: 3
for i in range(4,0,-1):
    for j in range(1,i+1):
        print(j,end=(''))
    print('')
print('\n')

#problem no: 4
for i in range(1,5):
    for j in range(1,i+1):
        print(i,end='')
    print('')
print('\n')

#problem no: 5
for i in range(4,0,-1):
    for j in range(i,0,-1):
        print(j,end='')
    print('')
print('\n')

#problem no: 6
for i in range(4,0,-1):
    for j in range(4,4-i,-1):
        print(j,end=(''))
    print(' ')
print('\n')

#problem no: 7
for i in range(1,5):
    for j in range(4,i,-1):
        print(end=(' '))
    for j in range(1,i+1):
        print(j,end=(''))
    print('')
print('\n')

#problem no: 8
for i in range(4,0,-1):
    for j in range(0,4-i):
        print(end=(' '))
    for j in range(1,i+1):
        print(j,end=(''))
    print('')
print('\n')

#problem no: 9
for i in range(1,5):
    for j in range(4,i,-1):
        print(end=' ')
    for j in range(1,i+1):
        print(j,end=' ')
    print('')
print('\n')

#problem no: 10
for i in range(1,5):
    for j in range(4,i,-1):
        print(end=' ')
    for j in range(1,i+1):
        print(j,end=' ')
    print('')
for i in range(4,1,-1):
    for j in range(0,5-i):
        print(end=' ')
    for j in range(1,i):
        print(j,end=' ')
    print('')
print('\n')

#problem no: 11
for i in range(1,6):
    for j in range(5,i,-1):
        print(end=' ')
    for j in range(1,i+1):
        print('*',end=' ')
    print('')
for i in range(5,1,-1):
    for j in range(0,6-i):
        print(end=' ')
    for j in range(1,i):
        print('*',end=' ')
    print('')
print('\n')

#problem no: 12
for i in range(1,5):
    print('*',end='')
    for j in range(1,i+1):
        print(j,end='')
    print('*',end='')
    print('')
print('\n')
