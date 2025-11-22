class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name)

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print(self.name)

if __name__ == '__main__':
    dog = Animal('Dog')
    dog.speak()
