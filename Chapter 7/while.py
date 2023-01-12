# #This will give error as condition is not satisfied, body will not be executed
i = 1
while i >10 :
    print("Yes")

# # #This will give infinite loop

i = 11
while i >10 :
    print("Yes")

# # In this body will be executed until conditioin is true

# #Example  1
i = 0
while i < 10 :
    print("Yes"+ str(i))    
    i = i+1
# #Example  2
i = 1
while i < 10 :
    print("Yes"+ str(i))    
    i = i+1

#Print numbers from 1 to 50
i=1
while i < 51 :
    print(i)  
    i=i+1

#Write a program to print content of list using while loops   

fruits = ["Orange","Apple","Banana"]
i = 0
while i<len(fruits):
    print(fruits[i])
    i = i + 1



