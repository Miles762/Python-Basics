class Employee:
    Company ="Google"

    def getsalary(self): #If we dont write self then this error is given " Takes O positional arguements but 1 is given"
        print(f"The salary is {self.salary} and emloyee works in {self.Company}")

harry = Employee() 
harry.salary=124
harry.getsalary()  #This is same as Employee.getsalary(harry)    