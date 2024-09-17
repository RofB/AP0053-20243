def opciones():
   print("Desee que operacion quiere realizar: \n1. Realizar suma \n2. Realizar resta \n3. Elevar al cuadrado \n4. Realizar multiplicación \n5. Realizar división")
   num = int(input("Ingrese la opcion de preferencia: "))
   return num


class cuadrado:
   def __init__(self,val):
      self.val=val
   def elev(self):
      return self.val*self.val
 
 
class operaciones:
   def __init__(self, a, b):
      self.a = int(input("Ingrese primer valor: "))
      self.b = int(input("Ingrese segundo valor: "))
   
   def sum(self):
      print(f"La suma de tus numeros es: {self.a + self.b}")

   def rest(self):
      return self.a - self.b
   
   def mult(self):
      return self.a * self.b
   
   def div(self):
      while self.b == 0 or type(self.b) != int:
         self.b = input("Ingrese segundo valor: ")
         print(type(self.b))
         
      return self.a/self.b
   def impr(self):
      print(self.a)