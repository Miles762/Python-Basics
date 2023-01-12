# Calculating factorial
n = 6
product =1

for i in range(n):
    product = product * (i +1)
print (product)



# Calculating factorial with help of function
def factorial(n) :
    product = 1
    for i in range (n) :
        product = product *(i+1)
    return (product)  

    
print(factorial(4))


# Calculating factorial with help of recursion
def recursion(n) :
    product = 1
    if n ==1 or n==0 :
        return 1
    else :
        return n * recursion (n-1)
print (recursion(3))



    
