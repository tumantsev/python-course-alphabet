from ruamel.yaml import YAML


class Leg:
    def __init__(self, weight=50, length=50):
        self.weight = weight
        self.age = length


class Animal:

    def __init__(self, name, age, leg):
        self.name = name
        self.age = age
        self.leg = leg

    def speak(self):
        return 'Moo'


leg = Leg()
cow = Animal('Milka', 5, leg)

yaml = YAML()
# yaml = ruamel.yaml.YAML()


yaml.register_class(Animal)
yaml.register_class(Leg)


with open('cow.yaml', 'w') as file:
    yaml.dump(cow, file)


with open('cow.yaml', 'r') as file:
    restore_animal = yaml.load(file)

print(restore_animal)