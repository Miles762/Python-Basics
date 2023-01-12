# # # #Q1 Find greater numbers among any 3 numbers

def maximum (num1,num2,num3) :
    if (num1 > num2 ) :
        if (num1 > num3) :
            return num1
        else :
            return num3  
    else :
        if (num2 > num3 ) :
            return num2
        else :
             return num3 

m = maximum(12,23,45)  
print("The value of maximum is "+ str(m))           
# # # #Q2 Convert celsius to farh

def farh(cel) :
    return (cel * (9/5)) + 32

c= 34
print("The fahreheit temperature is " + str(farh(c)))

#Q3 Prevent to print a new line at the end
print("Hello",end = " ")
print("Hardik",end = " ")
print("Hi",end = "\n ") #To get ans of next question in next line we use \n in the end
    
# # # #Q4 Sum of n natural numbers

def sum (n) :
    if n == 1 :
        return 1
    else :
        return  n + sum(n-1)

n= sum(3)
print("The sum of natural numbers is " + str(n))

# Print star 
n = 5
for i in range (n) :
    print("*" * (n-i))

# Remove a word from a string and spaces too
def removeandsplit(string,word):
    newStr = string.replace(word,"")
    return newStr.strip()

This =  "    Harry is a good boy   "
n = removeandsplit(This,"Harry")
print (n)

#Convert inches to cm
def cm(n) :
    return n*(5/2)
    
e = 4

print("The value in cm  is " + str(cm(e)))








