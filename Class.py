from statistics import mean
class Student:
    name  = ""
    email = ""
    grades = []


    def __init__(self,name="", email=""):
        self.name = name
        self.email = email
    
    def get_grade(self, grade):
        if grade >=0 and grade <=100:
            self.grades.append(grade)

    def getmin(self):
        return min(self.grades)

    def getmax(self):
        return max(self.grades)

    def mean_grades(self):
        return mean(self.grades)
  
    def __str__(self):
        return f'name:{self.name} mean:{self.mean_grades()} all grades: {self.grades}'

    
stu1 = Student(name="yuval",email="yuvalsha@gmail.com")
stu1.get_grade(91)
stu1.get_grade(65)
stu1.get_grade(-81)
stu1.get_grade(78)
print(stu1)




    
