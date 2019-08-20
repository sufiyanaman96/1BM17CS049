
list=[]
a=int(input("Enter the element : "))

while (a!=-1):
    list.append(a)
    a=int(input("Enter the element : "))
    

print("original_list : ",list)
even_list=[]
i=0
for i in range(len(list)) :
	if(i%2==1) :
		even_list.append(list[i])
print("even_list : ",even_list)
    
