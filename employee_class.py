from person_file import Person

class Employee(Person): #ירושה
    def __init__(self, id, name, age, field_of_work, salary):
        super().__init__(id, name, age)
        self.field_of_work = field_of_work
        self._salary = salary

    def getFieldOfWork(self):
        return self.field_of_work
    
    def getSalary(self):
        return self._salary
    
    def printEmployee(self):
        print(self.getPersonString() + " ,The field of work is " + self.getFieldOfWork() + 
              " ,The salary is " + str(self.getSalary()))

    def printMySelf(self):
        self.printEmployee()
            
    def myFunc(self):
        print("I am a employee")

    def foo(self):
        super().myFunc()

