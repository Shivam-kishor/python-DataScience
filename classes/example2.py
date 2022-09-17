class Employee:
    #constructor
    def __init__(self,name,desig,depth,salary,skills=None):
        self.name=name
        self.designation=desig
        self.department=depth
        self.salary=salary
        self.skills=skills

    def do_task(self,task):
            print(f"Employee{self.name} is doing {task}")


    def info(self):
            print("EMPLOYEE DETAILS")
            print(f'Name :{self.name}')
            print(f"Department : {self.department}")
            print(f"Desigination : {self.designation}")
            print(f"Salary  :{self.salary}")
            print(f"Skills : {self.skills}")


    def add_skill(self,skillname):
        if self.skills is None:
            self.skills=[skillname]
        else:
            self.skills.append(skillname)



e1=Employee('Raj','Assistant 2', 'Sales',40000,['Talking'])
e2=Employee('Sonu','Staff Officer','Finance',70000,['management','leadership'])        


e1.info()
e2.info()
e1.do_task("making some sales")
e2.do_task('firing employees')
e1.add_skill('helping')
e1.add_skill("confidence")

e1.info()