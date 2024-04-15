class Ptak:
    def __init__(self,age,):
        self.age = age
     
    def soundD(self,sound):
        self.sound = " beepbeep"
    


class Kura(Ptak):
    def __init__(self, age ,wage):
        self.age = age
        self.wage = wage

    def run(self,speed):
        self.speed = speed


class Orzel(Ptak):
    def __init__(self, age,wage):
        self.age=age
        self.wage = wage
    def run(self,speed):
        self.speed = speed

    def maxfly(self,distance,flightAltitude):
        self.distance=distance
        self.flightAltitude =flightAltitude
        print(f"Orzel moze przeleciec najwyzej {self.distance}, z maksymalna wysokoscia {self.flightAltitude}")



class Warrior:
   def __init__(self,name,hp,damage,distance):
       self.name= name
       self.damage= damage
       self.distance= distance

   def przedstawSie(self):
       print(f"Postac ma na imie {self.name}")

   def position(self,postioN):
       self.postioN =  (self.postion+self.distance)
       return self.positioN
class WarriorNinja(Warrior):
    def __init__(self, name, hp, damage, distance):
        super().__init__(name, hp, damage, distance)

    def skradanieSie(self,distanceOnShift):
        self.distanceOnShift= distanceOnShift
        self.distance = self.distance+self.distanceOnShift
        return self.distance
class WarriorArcher(Warrior):
    def __init__(self, name, hp, damage, distance,bow):
        super().__init__(name, hp, damage, distance)
        self.bow = False

    def ZalozLuk (self):
        self.bow= True
        return self.bow