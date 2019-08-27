def no_of_divisors( a ):
    for i in range (2, a//2):
        if ( a%i == 0 ):
            print(i)
a =int( input("Enter a number "))
no_of_divisors(a)
print (1)
print(0)
