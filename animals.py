class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def display_info(self):
        print(f'''
            Имя:{self.name}
            Вид:{self.species}
            Возраст:{self.age}
        ''')
    
    
    
    
bobik = Animal('Bobik','dog',3)
bobik.display_info()


class Shelter:
    animals = []
        
    def add_animal(self, animal):
        self.animals.append(animal)
    
    def show_animals(self):
        if len(self.animals) < 1:
            print('Приют пуст')
        else:
            for animal in self.animals:
                animal.display_info()
    def find_by_species(self,species_name):
        finded = False
        for animal in self.animals:
            if animal.species == species_name:
                animal.display_info()
                finded = True
        if not finded:
            print(f'животных вида {species_name} не найдено')
shelter = Shelter()
shelter.add_animal(bobik)
shelter.find_by_species('cat')
