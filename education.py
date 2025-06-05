class Student:
    def __init__(self, name, student_id):
        self.__name = name
        self.__student_id = student_id
        self.__grades = []
    
    def get_name(self):
        return self.__name
    
    def get_id(self):
        return self.__student_id
    
    def get_grades(self):
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
        return avg
        
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
    
    def find_by_name(self, name):
        finded = False
        for student in self.students:
            if name == student.get_name():
                print(f'Студент по имени {name} найден')
                student.display_info()
                finded = True
        
        if not finded:
            print(f'Студента по имени {name} нет в этой группе')
                
    def remove_student_by_id(self, student_id):
        finded = False
        for student in self.students:
            if student_id == student.get_id():
                print(f'Студент по имени {student.get_name()} исключен из группы')
                self.students.remove(student)
                finded = True
        
        if not finded:
            print(f'Студента с id {student_id} нет в этой группе')
                
                

class HonorsStudent(Student):
    def is_eligible_for_award(self):
        if self.get_average() >= 90:
            return True
    
    def display_info(self):
        if self.is_eligible_for_award():
            print(f'''
            Имя:{self.get_name()}
            ID:{self.get_id()}
            Претенднт на награду
            ''')
        else:
            print(f'''
            Имя:{self.__name}
            ID:{self.__student_id}
            ''')
            
alesha = HonorsStudent('Алеха', 12)
alesha.add_grade(99)
alesha.add_grade(95)
alesha.add_grade(89)
alesha.add_grade(100)
alesha.add_grade(92)
# alesha.get_average()


group = Group()

group.add_student(alesha)

alesha.is_eligible_for_award()
alesha.display_info()
# group.remove_student_by_id(112)
