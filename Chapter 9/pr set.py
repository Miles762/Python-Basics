# Q1) Find if twinkle is present
with open("sam.txt",) as f :
    t = f.read()
    if "twinkle " in t :
        print("twinkle is present")
    else :
        print("twinkle is not  present")

# Q2) Overwrite score if it is greater than value of highscore
def gamewin():
    return 4436
score = gamewin()
with open("highscore.txt") as f :
    highscore= f.read()
       
if (highscore) == "":
    with open ("highscore.txt","w") as f:
        f.write(str(score))
    
elif int(highscore)<score :
    with open ("highscore.txt","w") as f:
        f.write(str(score)) #We have use str coz f.write takes string not an integer 
      
# Q3)Print tables from 12 to 20
for i in range (12,21):
    with open(f"tables2/Multiplication table of {i}.txt","w") as f:
        for j in range (1,11) :
            f.write(f"{i}x{j}={i*j}\n")

# Q4 Replacing  a particular word with another word in a file
with open("donkey.txt") as f :
    cont=f.read()

cont = cont.replace("donkey","abc")
with open("donkey.txt","w") as f :
    f.write(cont)

#Q5 Replacing content of list with a particular word    
     
words = ["hardik","gud","boy","ads"]
with open("replaceee.txt") as f :
    cont=f.read()
for word in words:
    cont = cont.replace(word,"ab")
    with open("replaceee.txt","w") as f :
        f.write(cont)


#Q6 Find if a particular word is present in a log file
 
with open ("log.txt") as f :
    ad = f.read().lower() #.lower() read all content in lower case

if "python"  in ad :
    print("python is present")

else:
    print("python is not present")


#Q7 Find the line number in which a particular word is present in a log file
ad = "True"
i = 1
with open ("log.txt") as f :
    while ad :
        ad= f.readline() 

        if "python"  in ad :
            print(f"python is present on line {i}")
            
        i+=1


#Q8 Copy content of one file to another
with open ("happy.txt") as f :
    ed = f.read()

with open ("happy1.txt","w") as f :
    f.write(ed)

#Q9 Find if content of 2 files is same or not
with open("qwe.txt") as f :
    st=f.read()

with open("qwer.txt") as f :
    stre=f.read()

if st==stre :
    print("Contents of file are same")

else:
    print("Contents of files are not same")


#Q10) Wipe contents of a file
with open("wax.txt","w") as f:
    f.write("")

#Q11) Rename a file to pythoner.txt    
# We can imitate renaming a file by creating a new file with same content as old file and then deleting the old file
import os
oldname = "had.txt"
newname = "pythoner.txt"
with open(oldname) as f :
    dw = f.read()

with open(newname,"w") as f :
     f.write(dw)

os.remove(oldname)




   