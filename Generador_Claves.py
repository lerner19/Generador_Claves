import string
import random


def main():  
     print("**********Bienvenido**********")
     print("Seleccione una opcion")
     seleccion = O_Seleccion("1: Generar clave aletoria \n2: Generar clave mediante una frase \n")

     cantidad = O_cantidad("Ingrese la cantidad de claves a generar debe ser mayor a 0: ")
     longitud = O_longitud("Ingrese el tamano de la clave debe ser mayor a 0: ")
     
     
     if seleccion == 2:
        frase = str(input("Ingrese la frase sin espacios: "))
        Randomizerfrase(cantidad, longitud, frase)
     else:
        Randomizer(cantidad, longitud)
  
## Esta funcion valida que la seleccion sea un numero valido     
def O_Seleccion(mensaje, tipo=int, condicion=lambda x: x > 0):
     while True:
          try:    
               valor = tipo(input(mensaje))
               if condicion(valor):
                    return valor
               else:
                    print("Favor ingresar un valor valido")
          except ValueError:
               print("Entrada no válida. Inténtalo de nuevo.")
## Esta funcion valida que la cantidad sea un numero valido
def O_cantidad(mensaje, tipo=int, condicion=lambda x: x > 0):               
     while True:
          try:    
               valor = tipo(input(mensaje))
               if condicion(valor):
                    return valor
               else:
                    print("Favor ingresar un valor valido")
          except ValueError:
               print("Entrada no válida. Inténtalo de nuevo.")
## Esta funcion valida que la longitud sea un numero valido
def O_longitud(mensaje, tipo=int, condicion=lambda x: x > 0):               
     while True:
          try:    
               valor = tipo(input(mensaje))
               if condicion(valor):
                    return valor
               else:
                    print("Favor ingresar un valor valido")
          except ValueError:
               print("Entrada no válida. Inténtalo de nuevo.")

def Randomizer(cantidad, longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    for _ in range(cantidad):
        clave = "".join(random.choice(caracteres) for i in range(longitud))
        print("Clave generada: "+ clave)

def Randomizerfrase(cantidad, longitud, frase):
    for _ in range(cantidad):
        recoleccion = random.sample(frase, longitud)
        password = "".join(recoleccion)
        print("Clave generada: "+password)


if __name__ == "__main__":
    main()   