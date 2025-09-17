
def sumar (a,b):
     return a+b 

def restar (a,b):
    return a-b

def dividir (a,b):
    if b ==0:
        raise ZeroDivisionError (" No se puede dividir por cero ")
    return a/b

def multiplicar (a,b):
    return a*b

print ("-- Calculadora digital --\n")

print ( "¿Que tipo de operacion quiere realizar? \n")

try:
    opcion = int(input( "[1] Sumar -- [2] Restar -- [3] Dividir -- [4] Multiplicar  ----> "))
except ValueError:
    print("Error: La opcion ingresada debe ser un número")
    exit()

if opcion == 1:
       try:
            resultado = sumar(
                int(input("Ingrese el primer número --> ")), 
                int(input("Ingrese el segundo número --> "))
            )
            print(f"\n--- El resultado de su operación es {resultado} ---")
       except ValueError:
            print("Error: Los operandos deben ser números válidos.")
elif opcion == 2:
       try:
            resultado = restar(
                int(input("Ingrese el primer número --> ")), 
                int(input("Ingrese el segundo número --> "))
            )
            print(f"\n--- El resultado de su operación es {resultado} ---")
       except ValueError:
            print("Error: Los operandos deben ser números válidos.")
elif opcion == 3:
       try:
            resultado = dividir(
                int(input("Ingrese el primer número --> ")), 
                int(input("Ingrese el segundo número --> "))
            )
            print(f"\n--- El resultado de su operación es {resultado} ---")
       except ValueError:
            print("Error: Los operandos deben ser números válidos.")
elif opcion == 4:
       try:
            resultado = multiplicar(
                int(input("Ingrese el primer número --> ")), 
                int(input("Ingrese el segundo número --> "))
            )
            print(f"\n--- El resultado de su operación es {resultado} ---")
       except ValueError:
            print("Error: Los operandos deben ser números válidos.")
else:
    print(" Elija una opcion valida ")

    
