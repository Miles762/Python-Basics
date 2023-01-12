import random
def gamewin(comp,you) :
    if comp == you :
        return None
    elif comp == "s" :
        if you == "p" :
            return True
        elif you ==  "sc":
            return False
    elif comp == "p" :
        if you == "sc" :
            return True
        elif you == "s":
            return False
    elif comp == "sc" :
        if you == "s" :
            return True
        elif you ==  "p":
            return False
    

print("comp has chosen stone(s) ,paper(p) or scissor(sc)?")
rand = random.randint(1,3)
if rand == 1 :
    comp = "s"
elif rand == 2 :
    comp  = "p"
elif rand == 3 :
    comp  = "sc"

you = (input ("you have chosen stone(s) ,paper(p) or scissor(sc)?"))

print (f"Computer has  chosen {comp}")
print (f"You  have  chosen {you}")
a = gamewin(comp,you)

if a == None :
 print("Its a tie")
elif a is True:
    print("you won")
elif a is False :
    print("you lost")
    
        
                





