class Car():
    doors = 4
    wheels = 4
    color = "red"
    name = "Toyota"

    def speed(self, distance, time):
        velocity = distance * time
        return velocity

    def detail(self):
       return "{} has {} wheels and {} door  with a color of {}".format(self.name, self.wheels, self.doors, self.color)

car1 = Car()
print(car1.speed(750, 5))
print(car1.detail())

car2 = Car()
print("Car2 speed", car2.speed(200, 4))
car2.doors = 2
car2.color = "Black"
car2.name = "Lamboghini"
print("Car2 detail: ", car2.detail())
