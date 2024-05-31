class Student:
    def __init__(self, name, age, avg_grade):
        self.name = name
        self.age = age  
        self.avg_grade = avg_grade
    
    def __str__(self):
        return f"{self.name} is {self.age} years old and has an average grade of {self.avg_grade}"
    
class UniStudent:
    def __init__(self, university):
        super(Student, self).__init__()
        self.university = university
    
erkanat_mini = Student('erkanat', 51, 1)
erkanat_standard = UniStudent('erkanat', 51, 100)