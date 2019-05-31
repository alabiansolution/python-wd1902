class Fish():
    location ="Ocean"
    swim = True

fish1 = Fish()    
print(fish1.location)
print(fish1.swim)


class Car():
    doors = 4
    wheels = 4
    color = "red"
    name = "Toyota"


    def speed(self, distance, time):
        velocity = distance * time
        return velocity
    def detail(self):
      
        