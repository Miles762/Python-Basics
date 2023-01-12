class Employee :
    company = "google" #Class attribute
    salary = 123 #When we exexute the program we see 
    # instance attribute is given priorty over class attributes

harry = Employee()   #Object instantation
raj = Employee()
harry.salary = 456  # {These are
raj.salary =786    #  instance attributes}
Employee.company = "twitter"  #Changing the attributes

print(harry.company)    
print(raj.company)    

print(harry.salary)    
print(raj.salary)    
# Below line throws an error as address is not present in instance/class
# print(raj.address)    
