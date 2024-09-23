def opciones():
   print("Desee que operacion quiere realizar: \n1. Elevar numero al cuadrado \n2. Realizar suma \n3. Realizar resta \n4. Realizar multiplicación \n5. Realizar división")
   num = int(input("Ingrese la opcion de preferencia: "))
   return num


class cuadrado:
   def __init__(self):
      self.val = int(input("Ingrese valor a operar: "))
   def elev(self):
      print(f"El valor al cuadrado es: {self.val*self.val}")
 
 
class operaciones:
   def __init__(self):
      self.a = int(input("Ingrese primer valor: "))
      self.b = int(input("Ingrese segundo valor: "))
      #while self.b == 0 or type(self.b) != int:
      #   self.b = input("Ingrese segundo valor: ")
      #   print(type(self.b))
      
   def sum(self):
      print(f"La suma de tus numeros es: {self.a + self.b}")

   def rest(self):
      print(f"La resta de tus numeros es: {self.a - self.b}")
   
   def mult(self):
      print(f"La multiplicacion de tus numeros es: {self.a * self.b}")

   def div(self):
      print(f"La division de tus numeros es: {self.a / self.b}")