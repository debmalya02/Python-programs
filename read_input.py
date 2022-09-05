a = str(input("Enter the name of file in .txt extension : \n"))
with open(a,'r') as f:
    for x in f:
        print(x)

# line = f.readline()
# with open(a,'r') as f:
#   while(line != ""):
#       print(line)
#       line = f.readline()


#with open(a,'r') as f:
#   print(f.readlline())