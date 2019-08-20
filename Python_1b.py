
fib_list=[0,1]
n=int(input("how many do you want in the series : "))
for i in range(2,n) :
	fib_list.append(fib_list[i-2]+fib_list[i-1])

print(fib_list)
