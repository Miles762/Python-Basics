class Employee:
    

    def getsalary(self,signature) :
        print(f"The salary is {self.salary} and emloyee works in {self.Company}\n{signature}")
    @staticmethod
    def greet():
        print("Good Morning sir")

harry = Employee() 
harry.salary=124
harry.Company= "Twitter"

harry.getsalary("Thanksss")  
harry.greet()  
