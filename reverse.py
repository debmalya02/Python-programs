n=int(input('Enter the number: '))
i=n
r=0
while i>0:
    n = i%10
    r = (r*10)+n
    i = i//10
print('The reverse of the number is ',r)