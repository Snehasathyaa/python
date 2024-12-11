class Employee:
    company_name="ABCD"
    location="Calicut"
    def __init__(self, id, name,salary):
        self.emp_id=id
        self.emp_name=name
        self.emp_salary=salary
        
    def detail(self):
        print(self.emp_id,self.emp_name,self.emp_salary)


emp1=Employee(101,"Manu",50000)
emp2=Employee(102,"Hari",25000)

print("company : ",Employee.company_name,"    location : ",Employee.location)

emp1.detail()
emp2.detail()
