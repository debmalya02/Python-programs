a = str(input("Enter the name of the file in .txt extension :\n"))
with open(a,'a') as f:
    new = str(input("Enter your string to append :\n"))
    f.write("\n")
    f.write(new)
with open(a,'r') as f1:
    print("Your updated file is :\n")
    print(f1.read())