#Question 1
mydict ={"hardik":"good",
"boy":"girl","jim ":"pam"}
print("The list of all words whose meaning we can know is\n",mydict.keys() )
a= input("Choose a word whose meaning you want\n")
print("The meaning of the word is :",mydict.get(a))




# #Question 2
num1 = int(input("Enter num 1\n"))
num2 = int(input("Enter num 2\n"))
num3 = int(input("Enter num 3\n"))
num4 = int(input("Enter num 4\n"))
num5 = int(input("Enter num 5\n"))
num6 = int(input("Enter num 6\n"))
num7 = int(input("Enter num 7\n"))
num8 = int(input("Enter num 8\n"))

s={num1,num2,num3,num4,num5,num6,num7,num8}
print(s)

#Question 3
s = {18,"18"}
print(s) #Both will be printed as one is set while other is int
print(len(s)) 

#Question 4
s = set()
s.add(20)
s.add("20")
s.add(20.0)
print(s)
print(len(s)) #index will be 2 coz 20 and 20.0 will be counted same

# #Question 5
s = {}# Here s is empty dictionary
s = set() #Here s is an empty s

#Question 6
dict={}
a = input("Enter your favourite lang Hardik\n")
b = input("Enter your favourite lang Tejas\n")
c = input("Enter your favourite lang Akshit\n")
d = input("Enter your favourite lang Garvit\n")
dict["Hardik"] = a
dict["Tejas"] = b
dict["Akshit"] = c
dict["Garvit"] = d



print(dict)



