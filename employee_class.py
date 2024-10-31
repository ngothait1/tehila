from person_class import Person

class Employee(Person): #ירושה
    def __init__(self, id, name, age):
        super().__init__(id, name, age)
        self.field_of_work = input("Field of work: ")
        self._salary = input("Salary: ")

    def getFieldOfWork(self):
        return self.field_of_work
    
    def getSalary(self):
        return self._salary
    
    def printEmployee(self):
        print(self.getPersonString() + " ,The field of work is " + self.getFieldOfWork() + 
              " ,The salary is " + str(self.getSalary()))

    def printDetails(self, space=""):
        super().printDetails(space)
        print(space + "Field of work: " + self.getFieldOfWork())
        print(space + "Salary: " + str(self.getSalary()))

    def printMySelf(self):
        self.printEmployee()
            
    def printType(self):
        print("Type: employee")

    def printTypeSuper(self):
        super().myFunc()

    def getInfoDict(self):
        info_dict1 = super().getInfoDictSuper()
        info_dict2 = {"Field of work": self.getFieldOfWork(),"Salary": str(self.getSalary())}
        merge_dict = {"Type": "employee"} | info_dict1 | info_dict2
        return merge_dict
