class Animal:
    id_counter = 0
    def __init__(self, name, species, age):
        self._name = name
        self._species = species
        self._age = age
        Animal.id_counter += 1
        self.id = Animal.id_counter
        
    def get_name(self):
        return self._name
        
    def get_species(self):
        return self._species
        
    def get_age(self):
        return self._age
        
    def display_info(self):
        print(f'''
            Имя:{self._name}
            Вид:{self._species}
            Возраст:{self._age}
            {self.id}
        ''')
    
    
    
    
bobik = Animal('Bobik','dog',3)
lelik = Animal('lelik','cat',2)
sharik = Animal('sharik','dog',5)
# bobik.display_info()


class Shelter:
    animals = []
     
    def add_animal(self, animal):
        self.animals.append(animal)
        animal.id_counter += 1
        
    
    def show_animals(self):
        if len(self.animals) < 1:
            print('Приют пуст')
        else:
            for animal in self.animals:
                animal.display_info()
                
    
    def find_by_species(self,species_name):
        finded = False
        for animal in self.animals:
            if animal._species == species_name:
                animal.display_info()
                finded = True
        if not finded:
            print(f'животных вида {species_name} не найдено')

    def remove_by_name(self,name):
        finded = False
        for animal in self.animals:
            if animal._name == name:
                self.animals.remove(animal)
                print(f'животное с именем {name} уходит из нашего приюта(')
                finded = True
                break
        if not finded:
            print(f'животное с именем {name} не найдено')
            
            
shelter = Shelter()
shelter.add_animal(bobik)
shelter.add_animal(lelik)
shelter.add_animal(sharik)
# shelter.find_by_species('cat')
shelter.remove_by_name('Bobik')

shelter.show_animals()

class Cat(Animal):

    def __init__(self, name, species, age,is_indoor):
        self._name = name
        self._species = species
        self._age = age
        Animal.id_counter += 1
        self.id = Animal.id_counter
        self.is_indoor = is_indoor
        
    def display_info(self):
        indoor = ''
        if self.is_indoor:
            indoor = 'нет'
        else:
            indoor = 'да'
            
        print(f'''
            Имя:{self._name}
            Вид:{self._species}
            Возраст:{self._age}
            Уличное:{indoor}
            {self.id}
        ''')
        
shika = Cat('shika','cat',2, True)
shika.display_info()

