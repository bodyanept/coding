class Student:
    def __init__(self, name, student_id):
        self.__name = name
        self.__student_id = student_id
        self.__grades = []
    
    def get_name():
        return self.__name
    
    def get_id():
        return self.__get_id
    
    def get_grades():
        return self.__get_grades
        
        
    def display_info(self):
        print(f'''
        Имя:{self.__name}
        ID:{self.__student_id}
        ''')
    def add_grade(self, grade):
        self.__grades.append(grade)
        
    def get_average(self):
        avg = sum(self.__grades) / len(self.__grades)
        print(f'Средний балл студента {self.__name} составляет : {avg}')
        
class Group:
    def __init__(self):
        self.students = []
        
    def add_student(self,student):
        self.students.append(student)
        

    def show_students(self):
        if len(self.students) < 1:
            print('Группа пуста')
        else:
            for student in self.students:
                student.display_info()
        
