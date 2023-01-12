# question 1
num1 = int(input("Enter num1\n"))
num2 = int(input("Enter num2\n"))
num3 = int(input("Enter num3\n"))
num4 = int(input("Enter num4\n"))

if(num1>num4):
    f1=num1
else:
    f1=num4

if(num2>num3):
    f2=num2
else:
    f2=num3

if(f1>f2):
    print(str(f1) + " is greatest")
else:
    print(str(f2) + " is greatest")  


# question2
marks1  = int(input("Enter the percentage of marks in sub 1\n")) 
marks2  = int(input("Enter the percentage of marks in sub 2\n")) 
marks3  = int(input("Enter the percentage of marks in sub 3\n")) 

if (marks1<33 or marks2<33 or marks3<33):
    print("Student has failed as he was unable to secure more than 33 percent in one of the subjects ")

elif((marks1+marks2+marks3)/3<40):
    print("Student has failed as he was unable to secure more than 40 percent collectively in all of the subjects ")
else :
    print("Student passed")   

#question3

text = input("Enter the words\n")

if("buy now" in text) :
    spam = True
else:
    spam = False    
if("make a  lot of money" in text) :
    spam = True  
else:
    spam = False    
if("subscribe this" in text) :
    spam = True
else:
    spam = False     
if("click this" in text) :
    spam = True
else:
    spam = False 
if(spam == True):
    print("error")
else :
    print("no error")  


#question 4
a = input("Enter username\n")
print(len(a))

if(len(a)<10):
    print("username contains less than 10 characters")
else :
    print("username contains more than 10 characters")

#question 5
a = input("Enter username\n")
b =["hardik","shilpa","kumar","david"]

if(a in b):
    print("username is in the list ")
else :
    print("username is not in in the list ")

#question 6
marks  = int(input("Enter your marks\n")) 
if(marks>90):
    print("Grade is excellent")
elif(marks>=80):
    print("Grade is A")
elif(marks>=70):
    print("Grade is B")
elif(marks>=60):
    print("Grade is C")
elif(marks>=50):
    print("Grade is D")
else:
    print("Grade is f")





    

    
    


    