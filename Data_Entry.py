#Saving user inouts in a text file
def data_entry(f):
    file=open(f,"a")
    info=input("Enter information")
    file.writelines(info)
    file.writelines("\n")
    file.close()
    
def display(f):
    file=open(f,"r")
    content=file.read()
    print(content)
    file.close()
    
def size_file(f):
    file=open(f,"r")
    content=file.read()
    print("total size of file including space:",len(content))

print("""Menu
1. Information Entry
2.Display Information
3.Size of file
""")
while True:
    ch=int(input("Enter the choie"))
    if ch>=1 and ch<=3:
        fn=input("Enter the file name")
        filename=fn+'.txt'
        print(filename)
        if ch==1:
            data_entry(filename)
        elif ch==2:
            display(filename)
        elif ch==3:
            size_file(filename)
    else:
        print("Enter correct choice")
    cont=int(input("do you want to continue?(0/1)"))
    if cont==0:
        break
    elif cont==1:
        continue
            
