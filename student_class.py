from person_class import Person

class Student(Person): #ירושה
    def __init__(self, id, name, age):
        super().__init__(id, name, age)
        self.field_of_study = input("Field of study: ")
        self.year_of_study = input("Year of study: ")
        self.score_avg = input("Score average: ")

    def getFieldOfStudy(self):
        return self.field_of_study
    
    def getYearOfStudy(self):
        return self.year_of_study

    def getScoreAvg(self):
        return self.score_avg
    
    def printStudent(self):
        print(self.getPersonString() + " ,The field of study is " + self.getFieldOfStudy() + 
              " ,The year of study is " + str(self.getYearOfStudy()) + 
              " ,The score average is " + str(self.getScoreAvg()))

    def printDetails(self, space=""):
        super().printDetails(space)
        print(space + "Field of study: " + self.getFieldOfStudy())
        print(space + "Year of study: " + str(self.getYearOfStudy()))
        print(space + "Score average: " + str(self.getScoreAvg()))

    def printMySelf(self):
        self.printStudent()

    def printType(self):
        print("Type: student")

    def printTypeSuper(self):
        super().myFunc()

    def getInfoDict(self):
        info_dict1 = super().getInfoDictSuper()
        info_dict2 = {"Field of study": self.getFieldOfStudy(),"Year of study": str(self.getYearOfStudy()), 
                      "Score average": str(self.getScoreAvg())}
        merge_dict = {"Type": "student"} | info_dict1 | info_dict2
        return merge_dict