class Car:
    color="black"
    @staticmethod
    def start_car():
        print("car started")

    @staticmethod    
    def stop_car():
        print("car stopped")    



class ToyotaCar(Car):
    def __init__(self,name):
        self.name=name
        super().start_car()


# car1= ToyotaCar("fortuner")
# print(car1.color)


class Car2:
    def __init__(self,type):
        self.type=type

class ToyotaCar2(Car2):
    def __init__(self,name,type):
        super().__init__(type)
        self.name=name

c2=ToyotaCar2("fortuner","electric")
print(c2.type)