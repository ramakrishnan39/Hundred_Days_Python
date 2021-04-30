class Vehicle:


    def __init__(self):
        self.color = "Blue"

    def drive(self):
        print("Moving one place to another place")
    
    def break(self):


class Car(Vehicle):

    def __init__(self):
        super().__init__()
        self.num_tyres = 4

    def 