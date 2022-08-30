class Zoo:
    animals = []

    def __init__(self) -> None:
        pass

    def add_my_animal(self):
        for animal in self.animals:
            print(animal)

    def remove_my_animal(self):
        for animal in self.animals:
            self.remove_my_animal(animal)

    def animals_count(self):
        return len(self.animals)
    
    def __str__(self) -> str:
        return f'name:{self.name} age:{self.age} dangerous:{self.dangerous}'
    class Animals:
        name =""
        age = 0
        dangerous = True

animal = Zoo()
lion = animal.add_animal("simba", 16)
dog = animal.add_animal("lucky", 12)

animal(lion)

