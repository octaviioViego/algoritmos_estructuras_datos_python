"""
Desarrollar el algoritmo de Euclides para calcular el máximo común divisor (MCD) de dos
número entero.
"""

def calcular_divisor(numero_mayor,numero_menor):
    if numero_menor == 0:
        return  numero_mayor
    
    reciduo =   numero_mayor % numero_menor
    return calcular_divisor(numero_menor, reciduo)
    

def calcular_minimo_multiplo(numero_mayor,numero_menor):
    if numero_menor == 0:
        return  numero_mayor
    
    reciduo =   numero_mayor % numero_menor
    
    return numero_mayor * numero_menor // calcular_divisor(numero_menor, reciduo)



# Calculas los número
print("Calcular el maximo común divisor...")
numero_maximo = int(input("Número maximo: "))
numero_manimo = int(input("Número minimo: "))
print(f"El minimo común divisor es {calcular_divisor(numero_mayor=numero_maximo,numero_menor=numero_manimo)}")
print(f"El minimo común multiplo es {calcular_minimo_multiplo(numero_mayor=numero_maximo,numero_menor=numero_manimo)}")