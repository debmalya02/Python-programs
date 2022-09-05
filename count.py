#counting numbers of letters
'''
a = str(input("Enter the file name in .txt extension : \n"))
with open(a,'r') as f:
    line = f.readline()
    num = 0
    for i in line:
        num += len(line.split())
print("Total number of words are : ",num)
'''
#counting number of words
a = str(input("Enter the name of file in .txt extension :\n"))
with open(a,'r') as f:
    num = 0
    for line in f:
        num += len(line.split())
print("Total number of words are : ",num)

#Another method
'''
a = str(input("Enter the name of file in .txt extension :\n"))
with open(a,'r') as f:
    line = f.readline()
    num = 0
    while(line != ""):
        num += len(line.split())
        line = f.readline()
print("Total number of words are : ",num)
'''