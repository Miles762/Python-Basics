# READ
f = open("sample.txt","r")
data = f.read()
print(data)
f.close()


# We can also specify the number of characters we want to read
f = open("sample.txt") #Also by default the mode is r 
data = f.read(3)
print(data)
f.close()



#####Readline function
f = open("sample.txt","r")
#Reads first line
data = f.readline()
print(data)
#Reads second line
data = f.readline()
print(data)
#Reads third line
data = f.readline()
print(data)
#Reads fourth line
data = f.readline()
print(data)
f.close()

#We can also print a specific line
f = open("sample.txt","r")
data = f.readline(3)
print(data)
f.close()

