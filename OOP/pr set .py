#Q1)
class Programmers :
    Company = "Microsoft"

    def __init__(self,name,age) :
        pass
    
        self.name = name
        self.age  =  age
        

    def getinfo(self):
        print(f"The name of the programmmer working in {self.Company} is {self.name} and the age of programmer is {self.age}")    

Harry = Programmers("Harry","19")
Alka = Programmers("Alka","18")
Harry.getinfo()
Alka.getinfo()


#Q2
class Calculator :
    def __init__(self, num) :
        self.num = num

    def getsquare(self) :
        print(f"The square of {self.num} is {self.num **2}")    


    def getcube(self):
        print(f"The cube of {self.num} is {self.num  **3}") 

        
    def getsquareroot(self):
            print(f"The squareroot of {self.num} is {self.num **0.5}") 

a = Calculator(9)        
a.getsquare()
a.getcube()
a.getsquareroot()


#Q2
class Calculator :
    @staticmethod
    def greet():
        print("Hellooo")
    def __init__(self, num) :
        self.num = num

    def getsquare(self) :
        print(f"The square of {self.num} is {self.num **2}")    


    def getcube(self):
        print(f"The cube of {self.num} is {self.num  **3}") 

        
    def getsquareroot(self):
            print(f"The squareroot of {self.num} is {self.num **0.5}") 
    
a = Calculator(9)
a.greet() 
a.getcube()
a.getsquare()
a.getsquareroot()
    
#Train question

class Train :
    def __init__(self,Name,Fare,Seats) :
        self.Name = Name
        self.Fare= Fare
        self.Seats= Seats

    def noofseats(self):
        print(f"The numbers of seats in the train is {self.Seats}")
    def nameoftrain(self):
        print(f"The name of  the train is {self.Name}")
    def price(self):
        print(f"The price of the ticket is Rs {self.Fare}")
    def seatinfo (self) :
        if(self.Seats>1) :
            print(f"Your seat number is {self.Seats}")
            self.Seats = self.Seats - 1
        else :
             print("No seats ae available")

a =Train("Rajdhani Express",450,3)   
a.noofseats()
a.nameoftrain()
a.price()
a.seatinfo()
a.noofseats()
