class Employee:
    def __init__(self, name,surname,age,salary,num_of_hours):
        self.name = name
        self.surname = surname
        self.age = age
        self.salary= salary
        self.num_of_hours = num_of_hours
    def przedstawienieSie(self):
        print(f"Nazywam sie {self.name} {self.surname}, mam {self.age}")

    def podwyzka(self,bonus):
        self.bonus = bonus
        return (self.salary + self.bonus)
    

prac = Employee("Mati","kowalski",20,4000,120)
prac.przedstawienieSie()
print(prac.podwyzka(1000))

class Monster:
    def __init__(self, name, hp,damage):
        self.name = name
        self.hp = hp
        self.damage= damage

    def monInfro(self):
        print(f"Potwor to {self.name}, jego sila ataku to {self.hp} a i ma {self.damage} puntkow zycia")
    
    def fight(self,Monster):
        if self.hp > Monster.hp and self.damage > Monster.damage:
            print("Wygrales")

        else:
            print("Przegrales")
    def evolution(self,bonusHp,bonusDamage):
        self.bonusHP= bonusHp
        self.bonusDamage= bonusDamage
        self.hp = self.hp+self.bonusHP
        self.damage= self.damage+self.bonusDamage
        
potworek= Monster("wampir",20,30)
potworek.monInfro()
potw2= Monster("wikloka",12,15)
potworek.fight(potw2)

class Lodowka:
    def __init__(self,marka, minTemp,maxTemp,wiek,zawartosc):
        self.marka = marka
        self.minTemp = minTemp
        self.maxTemp=  maxTemp
        self.wiek = wiek
        self.zawartosc= zawartosc
    def nazwaLod(self):
        print(f"Lodowka jest firmy{self.marka}")

    def zdatnoscTemp(self,tempPro):
        self.tempPro = tempPro
        if self.tempPro > self.minTemp and self.tempPro< self.maxTemp:
            print("mozna trzymac ten prodkut w lodowce")

        else :
            print("nie mozna przetrzymac tego produktu w lodwce ")

    def zawartoscLod(self):
        zawTab=  [self.zawartosc.split(",")]
        print(zawTab)


lodowka = Lodowka("samsung",1,29,2,"lody,mleko,piwo,maslo")
lodowka.nazwaLod()
lodowka.zawartoscLod()