# # # # Q1 Print multiplication table of a givn number 
# num = int(input("Enter a number\n"))
# for i in range (1,11):
#     # print(str(num) + "x" + str(i) + "=" + str(i*num))
#      print (f"{num}X{i}={num*i}")


# # #Q2 Print names with only s starting     

# L1 = ["Harry","Sohan","Sohum","David"]
# for name in L1 :
#         if name.startswith("S") :
#             print("Hi" + name)

# #Question 3 Use while loop in quetion 1
# num = int(input("Enter a number\n"))
# i = 1 
# while i<11 :
#     # print(str(num) + "x" + str(i) + "=" + str(i*num))
#      print (f"{num}X{i}={num*i}")
#      i = i + 1

# #Question 4  Find if a number is prime or not   
# num = int(input("Enter the number\n"))
# prime = True
# for i in range (2,num) :
#     if num%i== 0 :
#         prime = False
#         break
# if prime is True :
#     print("The number is a prime number")    
# else :
#     print("The number is not a prime number")  


# #Question 6 Find the factorial of a number
# num = int(input("Enter the number\n"))
# factorial = 1
# for i  in range (1,num+1) :
#     factorial = factorial * i
# print(f"The factorial of {num} is {factorial}")

# #Q7 )Finding the sum of first n natural numbers using for loop

# num = int(input("Enter the number\n"))
# sum = 0
# for i in range (1,num +1) :
#     sum = sum + i
# print(f"The sum of first {num} natural numbers  is {sum}")

#Q7 )Finding the sum of first n natural numbers using while loop

num = int(input("Enter the number\n"))
sum = 0
i = 1
while i < (num +1 ) :
    sum = sum + i
    i = i + 1
print(f"The sum of first {num} natural numbers  is {sum}") 


    























