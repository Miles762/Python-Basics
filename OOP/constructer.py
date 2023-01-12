#Example of constructer taking  self arguement

class Employee:
    def __init__(self) :
        print("Hey there")
        

    def getsalary(self,signature) :
        print(f"The salary is {self.salary} and emloyee works in {self.Company}\n{signature}")
    @staticmethod
    def greet():
        print("Good Morning sir")

harry = Employee() 



#Example of constructer taking further arguements
class Employee:
    def __init__(self,age,date) :
        self.age = age
        self.date = date
        print("Hey there")

    def getdetails(self):
        print(f"The age of employee is {self.age}")
        print(f"Today's date  is {self.date}")

    

    # def getsalary(self,signature) :
    #     print(f"The salary is {self.salary} and emloyee works in {self.Company}\n{signature}")
    # @staticmethod
    # def greet():
    #     print("Good Morning sir")

harry = Employee("19","14th Oct") 
harry.getdetails()
# harry.salary=124
# harry.Company = "Youtube"
# harry.getsalary("OKayyyy")
# harry.greet()

