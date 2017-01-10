from person import Person


class Student(Person):
    def knowledge(self, knowledge_level):
        self.knowledge_level = knowledge_level
    
    def energy(self, energy_level):
        self.energy_level = energy_level
