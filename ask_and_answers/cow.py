import json
from pprint import pprint


class Cow:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_json(cls, data):
        cow = Cow(
            name=data.get('name'),
            age=data.get("age")
        )
        return cow


class Horse:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_json(cls, data):
        horse = Horse(
            name=data.get('name'),
            age=data.get("age")
        )
        return horse


class Zoo:

    def __init__(self, name, list_of_animals):
        self.name = name
        self.list_of_animals = list_of_animals

    def add_new_animal(self, animal):
        self.list_of_animals.append(animal)

    @classmethod
    def from_json(cls, data):
        name = data.get("name")
        list_of_animals = []
        for animal in data.get('list_of_animals'):
            if animal['__type__'] == "Cow":
                list_of_animals.append(Cow.from_json(animal))
            if animal['__type__'] == "Horse":
                list_of_animals.append(Horse.from_json(animal))
        zoo = Zoo(name=name, list_of_animals=list_of_animals)
        return zoo

horse = Horse('Jack', 10)
cow = Cow('Milka', 5)

zoo_animals = [horse, cow]
zoo = Zoo('Central Zoo', zoo_animals)


class ZooJson(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Zoo):
            return {'name': obj.name, 'list_of_animals': obj.list_of_animals}
        if isinstance(obj, Cow):
            return {'__type__': 'Cow', 'name': obj.name, 'age': obj.age}
        if isinstance(obj, Horse):
            return {'__type__': 'Horse', 'name': obj.name, 'age': obj.age}
        return json.JSONEncoder.default(self, obj)


print("\n" * 2)

encoded_zoo = json.dumps(zoo, cls=ZooJson)
pprint(encoded_zoo)
print("\n" * 2)
print(type(encoded_zoo), encoded_zoo)
print("\n" * 2)

decoded_zoo = Zoo.from_json(json.loads(encoded_zoo))
pprint(decoded_zoo)
