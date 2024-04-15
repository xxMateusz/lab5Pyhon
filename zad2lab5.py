class Turtle:
    def __init__(self, name, speed,__x):
        self.name= name 
        self.speed = speed
        self.__x= __x

    def say_name(self):
     print(f"Jestem zolw {self.name}, i moja szybkosc  to {self.speed}")

    def move(self, distance):
     self.distance = distance

    def get_position(self):
     return self.__x


zolw= Turtle("maciek",20,1)
zolw.get_position()
zolw.say_name()