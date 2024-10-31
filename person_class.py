class Person:
    def __init__(self, id, name, age):
        self._id = id
        self._name = name 
        self._age = age

    def getId(self):
        return self._id
    
    def getName(self):
        return self._name
    
    def getAge(self):
        return self._age

    def getPersonString(self):
        return "The person " + self.getName() + " is " + str(self.getAge()) + " years old"

    def printDetails(self, space=""):
        print(space + "ID: " + str(self.getId()))
        print(space + "Name: " + self.getName())
        print(space + "Age: " + str(self.getAge()))

    def printMySelf(self):
        print(self.getPersonString())

    def printType(self):
        print("Type: person")

    def getInfoDict(self):
        info_dict = {"Type": "person"} | self.getInfoDictSuper()
        return info_dict

    def getInfoDictSuper(self):
        info_dict = {"ID": self.getId(), "Name": self.getName(), "Age": self.getAge()}
        return info_dict
    
if __name__ == "__main__":
    print("You're running person_file.py")
    # testing
    test_id = 123
    test_name = "test_name"
    test_age = 100
    test_person = Person(test_id, test_name, test_age)
    if test_person.getId() != test_id:
        print("Error: Id should be " + str(test_id) + " ,but i get " + str(test_person.getId()))
    if test_person.getName() != test_name:
        print("Error: Name should be " + test_name + " ,but i get " + test_person.getName())
    if test_person.getAge() != test_age:
        print("Error: Age should be " + str(test_age) + " ,but i get " + str(test_person.getAge()))
else:
    print("You're running person_file as a module")
