class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        self.student_id =  self.name[0]+self.last_name+self.birth_year

student_ident = Student(input(),input(),input())
print(student_ident.student_id)



        # calculate the student_id here