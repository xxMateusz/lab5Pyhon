import math
class Trapez():

  def __innit (self,a,b,h):
   if a.isnumeric() is not True:
         raise ValueError("Wartosci musza byc cyframi")
   if a <= 0 or b <= 0 or h <= 0:
            raise ValueError("Długości boków muszą być dodatnie.")
   self.a = a 
   self.b = b 
   self.h = h
  def pole(self):
         
         return ((self.a + self.b)*self.h)/2
  def obwod(self):
      return self.a+self.b+self.b
  
  
class Prostokat():
    
    def __init__(self, a, b):
        if not a.isnumeric() or not b.isnumeric():
            raise ValueError("Wartości muszą być cyframi.")
        if int(a) <= 0 or int(b) <= 0:
            raise ValueError("Długości boków muszą być dodatnie.")
        self.a = int(a)
        self.b = int(b)
    
    def pole(self):
        return self.a * self.b
    
    def obwod(self):
        return self.a * 2 + self.b * 2

class kolo:
    def __init__(self, r):
         self.r = r 

    def pole(self):
         return math.pi * self.r**2
    def obwod(self):
         return math.pi * self.r *2



figura = ["prostokat","trapez","kolo"]
print(f"wybierz jedna z figur{figura}")

figuraUzytkownika = input()
print(figuraUzytkownika)
while figuraUzytkownika not in figura:
     figuraUzytkownika1=input()
     if figuraUzytkownika1 in figura:
          print("figura jest ok ")
          break
     elif figuraUzytkownika1 not in figura :
      input(f"Podaj poprawna figure ")

dane = input("podaj wymiary figury: bok wysokosc i promien jesli jest wymagana")
wymiary = dane.split(',')
if figuraUzytkownika in figura and figuraUzytkownika== figura[0]:
    if len(wymiary)!= 2 :
       while len(wymiary) != 2:
         dane= input("podaj poprawne wymiary prostkata:")
         wymiary1 = dane.split(',')
         if len(wymiary1) == 2:
                prostokat = Prostokat(wymiary1[0],wymiary1[1])
                prostkatP= prostokat.pole()
                print(f"pole prostokata wynosi {int(wymiary1[0]) * int(wymiary1[1])} {prostokatP} ")
                break    
    elif len(wymiary) ==2:
        a = wymiary[0]
        b = wymiary[1]
        prostokat = Prostokat(a, b)
        prostkatP= prostokat.pole()
        print(f"pole prostokata wynosi {prostkatP}")


elif figuraUzytkownika == figura[1]:
    if len(wymiary)!= 3 :
         while len(wymiary) != 3:
          dane= input("podaj poprawne wymiary trapezu w kolejnosci a,b,h:")
          wymiary1 = dane.split(',')
          if len(wymiary1) == 3:
              # trapez = T
               print(f"pole trapezu wynosi {(int(wymiary1[0]) + int(wymiary1[1]))* int(wymiary1[2]) * 1/2}")
               break    
    elif len(wymiary) ==3:
          print(f"pole trapezu wynosi {(int(wymiary[0]) + int(wymiary[1]))* int(wymiary[2]) * 1/2}")
    
elif figuraUzytkownika == figura[2]:
    if len(wymiary)!= 1 :
         while len(wymiary) != 1:
          dane= input("podaj poprawne wymiary kola czyli r")
          wymiary1 = dane.split(',')
          if len(wymiary1) == 1:
                print(f" pole kola wynosi {int(wymiary[0]) *int(wymiary[0]) * 3.14 }")
                break    
    elif len(wymiary) ==1:
         print(f" pole kola wynosi {int(wymiary[0]) *int(wymiary[0]) * 3.14 }")
    print(f" pole kola wynosi {int(wymiary[0]) *int(wymiary[0]) * 3.14 }")
