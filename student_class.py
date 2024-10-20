from person_file import Person

class Student(Person): #ירושה
    def __init__(self, id, name, age, field_of_study, year_of_study, score_avg):
        super().__init__(id, name, age)
        self.field_of_study = field_of_study
        self.year_of_study = year_of_study
        self.score_avg = score_avg

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

    def printMySelf(self):
        self.printStudent()

    def myFunc(self):
        print("I am a student")

    def foo(self):
        super().myFunc()