def search(lis,a):
    print (lis)
    if a in lis: return True
    else: return False

lis=[]
while True:
    a =int(input("Enter the element"))
    if a!=-1: lis.append(a)
    else: break

b =int(input("Enter element to search"))
x=search(lis,b)

if (x==True): print("Found")
else: print ("Not found")
