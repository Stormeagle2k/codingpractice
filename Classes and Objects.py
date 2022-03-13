class Animal:
    def __init__(self, legs, fur, sound,):
        self.legs = legs;
        self.fur = fur;
        self.sound = sound;
    def talk(self):
        print(self.sound)
class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self,4,True,"bark")
        self.name= name;
fido = Dog('Fido')
fido.talk()
print(fido.fur)
