# 1st basic method to calculate percentages

marks1 = [23,34,56,78]
percentage1 = (sum(marks1)/400) * 100



marks2 = [93,48,36,38]
percentage2 = (sum(marks2)/400) * 100
print(percentage1,percentage2)

# 2nd basic method to calculate percentages

marks1 = [23,34,56,78]
percentage1 = ((marks1[0]+ marks1[1]+marks1[2] +marks1[3])/400) * 100



marks2 = [93,48,36,38]
percentage1 = ((marks2[0]+ marks2[1]+marks2[2] +marks2[3])/400)  * 100

print(percentage1,percentage2)

# Calculating percentage with help of function

def man(marks):
  p =  (sum(marks)/400) * 100
  return p

  marks1 = [23,34,56,78]
percentage1 = man(marks1)



marks2 = [93,48,36,38]
percentage2 = man(marks2)
print(percentage1,percentage2)

#Greet someone with your name with help of fn
def greet(name ) :
    print(" Good Morning " + name)

greet("hardik")

#Add 2 numbers  with help of fn

def mysum(num1,num2) :
    return  num1 + num2

r = mysum (12,45)
print(r)


#Default Arguement
def greet(name = "pot") :
    print(" Good Morning " + name)

greet()
    

    




     
