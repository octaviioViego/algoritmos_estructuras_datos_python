"""
Desarrollar un algoritmo que permita calcular la seguiente serie:
h(n) = 1 + 1/2 + 1/3 .... 1/n 
"""

#Programa en python se divide por el numero de iteracion
def DivicionIteracion(numero_iteracion):
    if numero_iteracion == 1:
        return  1
    else:
        return (1/numero_iteracion) + DivicionIteracion(numero_iteracion-1)

#Solicitar el numero al usuario
numero_iteraciones = int(input("Ingresa el número de iteraciones: "))

suma_iteraciones = DivicionIteracion(numero_iteraciones)

print(f"La suma de las iteraciones es: {suma_iteraciones}")
